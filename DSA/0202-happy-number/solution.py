class Solution(object):
    def fun(self,n):
        s=0
        while n>0:
            r=n%10
            s=s+r*r
            n=n//10
        return s


    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        slow=fast=n
        while fast!=1:
            slow=self.fun(slow)
            fast=self.fun(fast)
            fast=self.fun(fast)
            if slow==fast and slow!=1:
                return False
        return True