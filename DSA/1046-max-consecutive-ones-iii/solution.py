class Solution(object):
    def longestOnes(self, nums, k):
        low = 0
        zero_count = 0
        res = 0
        for high in range(len(nums)):
            if nums[high] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[low] == 0:
                    zero_count -= 1
                low += 1
            length=high-low+1
            res = max(res,length)
        return res