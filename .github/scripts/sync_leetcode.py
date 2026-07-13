import os
import re
import sys
import time
from pathlib import Path

import requests


GRAPHQL_URL = "https://leetcode.com/graphql/"
BASE_URL = "https://leetcode.com"
SUBMISSIONS_URL = f"{BASE_URL}/api/submissions/"

EXTENSIONS = {
    "python": "py",
    "python3": "py",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "postgresql": "sql",
    "pandas": "py",
    "java": "java",
    "cpp": "cpp",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "ruby": "rb",
    "swift": "swift",
    "kotlin": "kt",
    "rust": "rs",
    "scala": "scala",
    "php": "php",
    "racket": "rkt",
    "erlang": "erl",
    "elixir": "ex",
    "dart": "dart",
}


class LeetCodeSyncError(RuntimeError):
    pass


def authentication_error(detail):
    return LeetCodeSyncError(
        f"LeetCode authentication failed: {detail} "
        "Refresh the LEETCODE_SESSION and LEETCODE_CSRF_TOKEN repository secrets "
        "from a currently signed-in leetcode.com browser session."
    )


def required_env(name):
    value = os.environ.get(name)
    if not value:
        raise LeetCodeSyncError(f"Missing required environment variable: {name}")
    return value


def cookie_secret_value(raw_value, cookie_name):
    value = raw_value.strip().strip('"').strip("'")
    value = re.sub(r"^cookie:\s*", "", value, flags=re.IGNORECASE)
    match = re.search(rf"(?:^|[;\s]){re.escape(cookie_name)}=([^;]+)", value, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return value


def describe_graphql_value(value):
    if isinstance(value, dict):
        return "object with keys: " + ", ".join(sorted(value.keys()))
    if isinstance(value, list):
        return f"list with {len(value)} item(s)"
    return type(value).__name__


def secret_format_description(raw_value, cookie_name):
    value = raw_value.strip().strip('"').strip("'")
    parsed_value = cookie_secret_value(value, cookie_name)
    if re.search(rf"(?:^|[;\s]){re.escape(cookie_name)}=", value, re.IGNORECASE):
        format_name = "cookie header"
    else:
        format_name = "raw value"
    return f"{format_name}, parsed length {len(parsed_value)}"


def slugify(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def problem_folder(question_id, title_slug, title):
    number = str(question_id or "0000").zfill(4)
    slug = title_slug or slugify(title or "leetcode-problem")
    return f"{number}-{slug}"


def extension_for(lang):
    return EXTENSIONS.get((lang or "").replace(" ", "").lower(), "txt")


def graphql_headers(session_cookie, csrf_token):
    return {
        "accept": "application/json",
        "content-type": "application/json",
        "origin": BASE_URL,
        "referer": f"{BASE_URL}/problemset/",
        "user-agent": "Mozilla/5.0 (compatible; leetcode-sync-workflow)",
        "x-requested-with": "XMLHttpRequest",
        "x-csrftoken": csrf_token,
        "cookie": f"csrftoken={csrf_token}; LEETCODE_SESSION={session_cookie}",
    }


def install_cookies(http, session_cookie, csrf_token):
    for domain in ("leetcode.com", ".leetcode.com"):
        http.cookies.set("LEETCODE_SESSION", session_cookie, domain=domain, path="/")
        http.cookies.set("csrftoken", csrf_token, domain=domain, path="/")


def post_graphql(http, headers, query, variables):
    response = http.post(
        GRAPHQL_URL,
        headers=headers,
        json={"query": query, "variables": variables},
        timeout=30,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        body = response.text.strip()
        detail = f": {body[:500]}" if body else ""
        if response.status_code in (401, 403):
            raise authentication_error(
                f"GraphQL returned HTTP {response.status_code}{detail}."
            ) from exc
        raise LeetCodeSyncError(
            f"LeetCode GraphQL HTTP {response.status_code} error{detail}"
        ) from exc
    payload = response.json()
    if payload.get("errors"):
        messages = "; ".join(error.get("message", str(error)) for error in payload["errors"])
        raise LeetCodeSyncError(f"LeetCode GraphQL error: {messages}")
    return payload.get("data") or {}


def fetch_submission_page(http, headers, offset, limit):
    queries = [
        (
            "submissionList",
            """
                        query submissions($offset: Int!, $limit: Int!) {
                            submissionList(offset: $offset, limit: $limit) {
                lastKey
                hasNext
                submissions {
                  id
                  lang
                  langName
                  timestamp
                  statusDisplay
                  title
                  titleSlug
                }
              }
            }
            """,
        ),
    ]

    last_error = None
    for field_name, query in queries:
        try:
            data = post_graphql(
                http,
                headers,
                query,
                {"offset": offset, "limit": limit},
            )
        except LeetCodeSyncError as exc:
            last_error = exc
            continue

        page = data.get(field_name)
        submissions = page.get("submissions") if isinstance(page, dict) else None
        if isinstance(page, dict) and isinstance(submissions, list):
            return page
        if isinstance(page, dict) and submissions is None:
            last_error = authentication_error(
                f"GraphQL returned {field_name}.submissions as null."
            )
            continue
        last_error = LeetCodeSyncError(
            f"LeetCode response did not include an iterable {field_name}.submissions list "
            f"({field_name} is {describe_graphql_value(page)}; "
            f"submissions is {describe_graphql_value(submissions)})."
        )

    try:
        return fetch_rest_submission_page(http, headers, offset, limit)
    except LeetCodeSyncError as exc:
        if last_error:
            raise LeetCodeSyncError(f"{last_error} REST fallback also failed: {exc}") from exc
        raise


def fetch_rest_submission_page(http, headers, offset, limit):
    response = http.get(
        SUBMISSIONS_URL,
        headers={key: value for key, value in headers.items() if key != "content-type"},
        params={"offset": offset, "limit": limit},
        timeout=30,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        body = response.text.strip()
        detail = f": {body[:500]}" if body else ""
        if response.status_code in (401, 403):
            raise authentication_error(f"REST returned HTTP {response.status_code}{detail}.") from exc
        raise LeetCodeSyncError(f"LeetCode REST HTTP {response.status_code} error{detail}") from exc

    payload = response.json()
    submissions = payload.get("submissions_dump")
    if not isinstance(submissions, list):
        raise LeetCodeSyncError(
            "LeetCode REST response did not include submissions_dump "
            f"(got {describe_graphql_value(submissions)}; response is {describe_graphql_value(payload)})."
        )

    normalized = []
    for submission in submissions:
        normalized.append(
            {
                "id": submission.get("id"),
                "lang": submission.get("lang") or submission.get("lang_name"),
                "langName": submission.get("lang_name") or submission.get("lang"),
                "timestamp": submission.get("timestamp"),
                "statusDisplay": submission.get("status_display") or submission.get("statusDisplay"),
                "title": submission.get("title"),
                "titleSlug": submission.get("title_slug") or submission.get("titleSlug"),
                "code": submission.get("code"),
                "questionId": submission.get("question_id") or submission.get("questionId"),
            }
        )

    return {
        "hasNext": bool(payload.get("has_next")),
        "lastKey": payload.get("last_key"),
        "submissions": normalized,
    }


def validate_login(http, headers):
    query = """
    query userStatus {
      userStatus {
        isSignedIn
        username
      }
    }
    """
    data = post_graphql(http, headers, query, {})
    user_status = data.get("userStatus") or {}
    return user_status.get("username") if user_status.get("isSignedIn") else None


def fetch_submission_details(http, headers, submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang
        question {
          questionId
          title
          titleSlug
        }
      }
    }
    """
    data = post_graphql(http, headers, query, {"submissionId": int(submission_id)})
    details = data.get("submissionDetails")
    if not isinstance(details, dict) or not details.get("code"):
        raise LeetCodeSyncError(f"Could not fetch code for submission {submission_id}.")
    return details


def write_submission(destination, submission, details):
    question = details.get("question") or {}
    lang = details.get("lang") or submission.get("lang") or submission.get("langName")
    folder = destination / problem_folder(
        question.get("questionId"),
        question.get("titleSlug") or submission.get("titleSlug"),
        question.get("title") or submission.get("title"),
    )
    folder.mkdir(parents=True, exist_ok=True)

    file_path = folder / f"solution.{extension_for(lang)}"
    code = details["code"].replace("\r\n", "\n")
    if file_path.exists() and file_path.read_text(encoding="utf-8") == code:
        return False, file_path

    file_path.write_text(code, encoding="utf-8")
    return True, file_path


def main():
    raw_csrf_token = required_env("LEETCODE_CSRF_TOKEN")
    raw_session_cookie = required_env("LEETCODE_SESSION")
    csrf_token = cookie_secret_value(raw_csrf_token, "csrftoken")
    session_cookie = cookie_secret_value(raw_session_cookie, "LEETCODE_SESSION")
    destination = Path(os.environ.get("DESTINATION_FOLDER", "DSA"))
    max_pages = int(os.environ.get("MAX_PAGES", "10"))
    page_size = int(os.environ.get("PAGE_SIZE", "20"))

    destination.mkdir(parents=True, exist_ok=True)
    headers = graphql_headers(session_cookie, csrf_token)
    http = requests.Session()
    install_cookies(http, session_cookie, csrf_token)

    seen_problem_lang = set()
    written = 0
    checked = 0

    print(
        "Secret formats: "
        f"LEETCODE_SESSION is {secret_format_description(raw_session_cookie, 'LEETCODE_SESSION')}; "
        f"LEETCODE_CSRF_TOKEN is {secret_format_description(raw_csrf_token, 'csrftoken')}.",
        flush=True,
    )
    try:
        username = validate_login(http, headers)
    except LeetCodeSyncError as exc:
        username = None
        print(f"LeetCode userStatus check failed: {exc}", flush=True)
    if username:
        print(f"Authenticated to LeetCode as {username}.", flush=True)
    else:
        print("LeetCode userStatus did not report a signed-in user; trying submissions endpoints.", flush=True)

    for page_index in range(max_pages):
        offset = page_index * page_size
        print(f"Fetching LeetCode submissions at offset {offset}...", flush=True)
        page = fetch_submission_page(http, headers, offset, page_size)
        submissions = page.get("submissions", [])

        for submission in submissions:
            if submission.get("statusDisplay") != "Accepted":
                continue

            key = (submission.get("titleSlug") or submission.get("title"), submission.get("lang"))
            if key in seen_problem_lang:
                continue
            seen_problem_lang.add(key)

            if submission.get("code"):
                details = {
                    "code": submission["code"],
                    "lang": submission.get("lang") or submission.get("langName"),
                    "question": {
                        "questionId": submission.get("questionId"),
                        "title": submission.get("title"),
                        "titleSlug": submission.get("titleSlug"),
                    },
                }
            else:
                details = fetch_submission_details(http, headers, submission["id"])
            changed, path = write_submission(destination, submission, details)
            checked += 1
            if changed:
                written += 1
                print(f"Wrote {path}")
            time.sleep(0.2)

        if not page.get("hasNext"):
            break

    print(f"Checked {checked} accepted submissions; wrote {written} file(s).")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"LeetCode sync failed: {exc}", file=sys.stderr)
        sys.exit(1)
