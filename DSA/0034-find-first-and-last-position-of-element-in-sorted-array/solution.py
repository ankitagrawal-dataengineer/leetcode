class Solution(object):
    def binarySearch(self,nums,target,first):
        low,high=0,len(nums)-1
        ans=-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]<target:
                low=guess+1
            elif nums[guess]>target:
                high=guess-1
            else:
                ans=guess
                if first:
                    high=guess-1
                else:
                    low=guess+1
        return ans

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=self.binarySearch(nums,target,True)
        last=self.binarySearch(nums,target,False)
        return [first,last]