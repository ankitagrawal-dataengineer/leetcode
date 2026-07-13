class Solution(object):
    def maxsum(self,nums):
        bestending=ans1=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=bestending+nums[i]
            bestending=max(v1,v2)
            ans1=max(ans1,bestending)
        return ans1

    def minsum(self,nums):
        bestending=ans2=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=bestending+nums[i]
            bestending=min(v1,v2)
            ans2=min(ans2,bestending)
        return ans2

    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v1=abs(self.maxsum(nums))
        v2=abs(self.minsum(nums))
        ans=max(v1,v2)
        return ans