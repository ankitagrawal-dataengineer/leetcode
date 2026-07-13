class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        off=2
        cm=2
        n=len(nums)
        while cm<n:
            if nums[cm]==nums[off-2]:
                cm+=1
                continue
            else:
                nums[off]=nums[cm]
                off+=1
                cm+=1
        return off