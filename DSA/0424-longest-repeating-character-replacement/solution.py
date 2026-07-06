class Solution(object):

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low=0
        n=len(s)
        freq={}
        max_count,res=0,0
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            length=high-low+1
            max_count=max(max_count,freq[s[high]])
            diff=length-max_count
            if diff>k:
                freq[s[low]]-=1
                low+=1
            length=high-low+1
            res=max(res,length)
        return res
