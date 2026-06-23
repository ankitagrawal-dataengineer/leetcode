class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        n=len(nums)
        j=n-1
        k=n-1
        a=[0]*n
        while i<=j:
            isq=nums[i]*nums[i]
            jsq=nums[j]*nums[j]
            if isq>=jsq:
                a[k]=isq
                i+=1
            else:
                a[k]=jsq
                j-=1
            k-=1
        return a

