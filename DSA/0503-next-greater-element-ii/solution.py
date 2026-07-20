class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        res=[-1]*n
        for i in range(n-2,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            stack.append(nums[i])
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            else:
                res[i]=-1
            stack.append(nums[i])
        return res