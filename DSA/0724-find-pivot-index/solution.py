class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        total=sum(nums)
        for i in range(len(nums)):
            right=total-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1
