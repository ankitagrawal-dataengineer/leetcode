class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low,high,s=0,0,0
        n=len(nums)
        max_len=float('inf')
        for high in range(n):
            s=s+nums[high]
            while s>=target:
                length=high-low+1
                max_len=min(max_len,length)
                s=s-nums[low]
                low+=1
        if max_len==float('inf'):
            return 0
        else:
            return max_len
