class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        low=0
        freq={}
        n=len(fruits)
        res=0
        for high in range(n):
            fruit=fruits[high]
            freq[fruit]=freq.get(fruit,0)+1
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            length=high-low+1
            res=max(length,res)
        return res

