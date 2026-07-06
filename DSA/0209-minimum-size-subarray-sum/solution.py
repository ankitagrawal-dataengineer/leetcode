class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low,window_sum=0,0
        res=float('inf')
        for high in range(n):
            window_sum+=nums[high]
            while window_sum>=target:
                length=high-low+1
                res=min(res,length)
                window_sum-=nums[low]
                low+=1
        if res==float('inf'):
            return 0
        else:
            return res
