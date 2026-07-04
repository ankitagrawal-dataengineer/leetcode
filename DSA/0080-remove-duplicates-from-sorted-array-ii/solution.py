class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        off = 2
        for cm in range(2, len(nums)):
            if nums[cm] != nums[off - 2]:
                nums[off] = nums[cm]
                off += 1
        return off
