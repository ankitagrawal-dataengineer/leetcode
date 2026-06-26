class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        a=[0]*n
        i,j,k=0,n-1,n-1
        while i<=j:
            isq=nums[i]*nums[i]
            jsq=nums[j]*nums[j]
            if isq<=jsq:
                a[k]=jsq
                j-=1
            else:
                a[k]=isq
                i+=1
            k-=1
        return a


