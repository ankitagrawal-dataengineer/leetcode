class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<high:
            guess=(low+high)//2
            if nums[guess]<nums[guess+1]:
                low=guess+1
            else:
                high=guess
        return low