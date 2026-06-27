class Solution(object):
    def bool_sahi(self, have, need):
        for ch in need:
            if have.get(ch, 0) < need[ch]:
                return False
        return True

    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        need = {}
        have = {}
        # Build frequency map of t
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        low = 0
        res = float('inf')
        start = -1
        for high in range(len(s)):
            have[s[high]] = have.get(s[high], 0) + 1

            while self.bool_sahi(have, need):
                length = high - low + 1

                if length < res:
                    res = length
                    start = low

                have[s[low]] -= 1
                low += 1

        if start == -1:
            return ""

        return s[start:start + res]