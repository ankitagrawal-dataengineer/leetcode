class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending=min_ending=best_ending=ans=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=nums[i]*max_ending
            v3=nums[i]*min_ending
            max_ending=max(v1,max(v2,v3))
            min_ending=min(v1,min(v2,v3))
            ans=max(ans,max(max_ending,min_ending))
        return ans
