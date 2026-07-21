class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low,high=0,len(arr)-1
        while low<=high:
            guess=(low+high)//2
            if arr[guess]<arr[guess+1]:
                low=guess+1
            else:
                ans=guess
                high=guess-1
        return ans