class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low,high,res=0,n-1,0
        while low<=high:
            guess=(low+high)//2
            if nums[guess]>nums[n-1]:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return nums[res]