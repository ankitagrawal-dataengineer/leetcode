class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        off,cm=2,2
        while cm<len(nums):
            if nums[cm]==nums[off-2]:
                cm+=1
                continue
            else:
                nums[off]=nums[cm]
                cm+=1
                off+=1
        return off