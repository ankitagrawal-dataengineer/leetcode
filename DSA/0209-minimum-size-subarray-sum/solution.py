class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low,window_sum=0,0
        min_len=float('inf')
        for high in range(n):
            window_sum+=nums[high]
            while window_sum>=target:
                length=high-low+1
                min_len=min(min_len,length)
                window_sum-=nums[low]
                low+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
