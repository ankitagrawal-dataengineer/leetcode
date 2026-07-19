class Solution:
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
    def maxSubarraySumCircular(self, nums):
        max_sum=self.maxsum(nums)
        min_sum=self.minsum(nums)
        total_sum=sum(nums)
        if min_sum == total_sum:
            return max_sum
        return max(max_sum, total_sum - min_sum)