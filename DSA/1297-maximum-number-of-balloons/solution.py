class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        have,need={},{}
        res=float('inf')
        for i in range(len(text)):
            have[text[i]]=have.get(text[i],0)+1
        bal='balloon'
        for i in range(len(bal)):
            need[bal[i]]=need.get(bal[i],0)+1
        for ch in need:
            if ch not in have:
                return 0
            else:
                res = min(res, have[ch] // need[ch])
        return res
        