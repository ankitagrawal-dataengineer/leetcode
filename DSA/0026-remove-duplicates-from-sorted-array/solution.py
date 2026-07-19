class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        off,cm=0,1
        n=len(nums)
        while cm<n:
            if nums[cm]==nums[cm-1]:
                cm+=1
                continue
            else:
                nums[off+1]=nums[cm]
                off+=1
                cm+=1
        return off+1