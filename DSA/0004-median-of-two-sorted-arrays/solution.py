class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums1 + nums2)  
        n = len(l)  
        if n % 2 == 1:
            return l[n // 2] 
        return (l[n // 2 - 1] + l[n // 2]) / 2 

