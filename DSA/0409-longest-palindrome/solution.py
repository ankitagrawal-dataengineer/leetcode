class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        ans = 0
        odd = False
        for count in freq.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1
                odd = True
        if odd:
            ans += 1
        return ans