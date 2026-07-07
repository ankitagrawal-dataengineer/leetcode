class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending=min_ending=best_ending=ans=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=max_ending*nums[i]
            v3=min_ending*nums[i]
            max_ending=max(v1,max(v2,v3))
            min_ending=min(v1,min(v2,v3))
            best_ending=max(max_ending,min_ending)
            ans=max(ans,best_ending)
        return ans
