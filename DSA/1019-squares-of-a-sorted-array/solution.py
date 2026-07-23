class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        i,j,k=0,n-1,n-1
        res=[0]*n
        while i<=j:
            isq=nums[i]*nums[i]
            jsq=nums[j]*nums[j]
            if isq>jsq:
                res[k]=isq
                i+=1
            else:
                res[k]=jsq
                j-=1
            k-=1
        return res
