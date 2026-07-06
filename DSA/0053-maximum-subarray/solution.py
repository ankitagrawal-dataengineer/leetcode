class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=best_ending=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=best_ending+nums[i]
            best_ending=max(v1,v2)
            ans=max(ans,best_ending)
        return ans
