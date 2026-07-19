class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n=len(fruits)
        low=res=0
        freq={}
        for high in range(n):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            length=high-low+1
            res=max(res,length)
        return res