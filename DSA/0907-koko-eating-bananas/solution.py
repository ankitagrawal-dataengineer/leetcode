class Solution(object):
    def fun(self,piles,n,speed):
        h=0
        for i in range(n):
            h+=piles[i]/speed
            if piles[i]%speed!=0:
                h+=1
        return h

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low,high=1,max(piles)
        n,res=len(piles),-1
        while low<=high:
            guess=(low+high)//2
            hour=self.fun(piles,n,guess)
            if hour>h:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res