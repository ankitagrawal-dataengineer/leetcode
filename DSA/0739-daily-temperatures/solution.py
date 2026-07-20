class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]-i
            else:
                res[i]=0
            stack.append(i)
        return res