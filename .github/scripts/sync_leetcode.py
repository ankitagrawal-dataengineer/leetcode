import os
import re
import sys
import time
from pathlib import Path

import requests


GRAPHQL_URL = "https://leetcode.com/graphql/"
BASE_URL = "https://leetcode.com"

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


def required_env(name):
    value = os.environ.get(name)
    if not value:
        raise LeetCodeSyncError(f"Missing required environment variable: {name}")
    return value


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
        "content-type": "application/json",
        "origin": BASE_URL,
        "referer": BASE_URL,
        "user-agent": "Mozilla/5.0 leetcode-sync-workflow",
        "x-csrftoken": csrf_token,
        "cookie": f"csrftoken={csrf_token}; LEETCODE_SESSION={session_cookie}",
    }


def post_graphql(http, headers, query, variables):
    response = http.post(
        GRAPHQL_URL,
        headers=headers,
        json={"query": query, "variables": variables},
        timeout=30,
    )
    response.raise_for_status()
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
            query submissions($offset: Int!, $limit: Int!, $slug: String) {
              submissionList(offset: $offset, limit: $limit, questionSlug: $slug) {
                hasNext
                submissions {
                  id
                  lang
                  timestamp
                  statusDisplay
                  title
                  titleSlug
                }
              }
            }
            """,
        ),
        (
            "questionSubmissionList",
            """
            query submissions($offset: Int!, $limit: Int!, $slug: String) {
              questionSubmissionList(offset: $offset, limit: $limit, questionSlug: $slug) {
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
                {"offset": offset, "limit": limit, "slug": None},
            )
        except LeetCodeSyncError as exc:
            last_error = exc
            continue

        page = data.get(field_name)
        if isinstance(page, dict) and isinstance(page.get("submissions"), list):
            return page
        last_error = LeetCodeSyncError(
            f"LeetCode response did not include an iterable {field_name}.submissions list. "
            "Refresh LEETCODE_SESSION and LEETCODE_CSRF_TOKEN if this continues."
        )

    raise last_error or LeetCodeSyncError("Unable to fetch submissions from LeetCode.")


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
    csrf_token = required_env("LEETCODE_CSRF_TOKEN")
    session_cookie = required_env("LEETCODE_SESSION")
    destination = Path(os.environ.get("DESTINATION_FOLDER", "DSA"))
    max_pages = int(os.environ.get("MAX_PAGES", "10"))
    page_size = int(os.environ.get("PAGE_SIZE", "20"))

    destination.mkdir(parents=True, exist_ok=True)
    headers = graphql_headers(session_cookie, csrf_token)
    http = requests.Session()

    seen_problem_lang = set()
    written = 0
    checked = 0

    for page_index in range(max_pages):
        offset = page_index * page_size
        print(f"Fetching LeetCode submissions at offset {offset}...")
        page = fetch_submission_page(http, headers, offset, page_size)
        submissions = page.get("submissions", [])

        for submission in submissions:
            if submission.get("statusDisplay") != "Accepted":
                continue

            key = (submission.get("titleSlug") or submission.get("title"), submission.get("lang"))
            if key in seen_problem_lang:
                continue
            seen_problem_lang.add(key)

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
