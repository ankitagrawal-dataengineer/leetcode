class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        need,have={},{}
        res=float('inf')
        for ch in text:
            have[ch]=have.get(ch,0)+1
        bal='balloon'
        for ch in bal:
            need[ch]=need.get(ch,0)+1
        
        for ch in need:
            res=min(res,have.get(ch,0)//need[ch])
        return res