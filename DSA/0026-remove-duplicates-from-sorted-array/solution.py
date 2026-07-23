class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        off,cm=0,1
        while cm<len(nums):
            if nums[cm]==nums[cm-1]:
                cm+=1
            else:
                nums[off+1]=nums[cm]
                off+=1
                cm+=1
        return off+1