class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        i,j=0,n-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [i+1,j+1]