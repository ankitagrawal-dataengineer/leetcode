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
        
        balloon='balloon'
        for ch in balloon:
            need[ch]=need.get(ch,0)+1
        
        for ch in need:
            if ch not in have:
                return 0
            else:
                res=min(res,have[ch]//need[ch])
        return res