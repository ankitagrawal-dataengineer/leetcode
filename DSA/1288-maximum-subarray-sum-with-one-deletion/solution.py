class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nopower=res=arr[0]
        power=0
        for i in range(1,len(arr)):
            v1=arr[i]
            v2=nopower+arr[i]
            v3=power+arr[i]
            v4=nopower
            nopower=max(v1,v2)
            power=max(v3,v4)
            res=max(res,max(nopower,power))
        return res