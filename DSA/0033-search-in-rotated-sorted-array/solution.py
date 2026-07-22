class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            guess=(low+high)//2

            if nums[guess]==target:
                return guess

            # guess is in left part
            if nums[guess] >= nums[0]:
                if target >= nums[0] and target < nums[guess]:
                    high = guess - 1
                else:
                    low = guess + 1

            # guess is in right part
            else:
                if target <= nums[n - 1] and target > nums[guess]:
                    low = guess + 1
                else:
                    high = guess - 1

        return -1