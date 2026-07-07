class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nodelete=ans=arr[0]
        onedelete=0
        for i in range(1,len(arr)):
            prevnodelete=nodelete
            prevonedelete=onedelete
            nodelete=max(nodelete+arr[i],arr[i])
            if prevonedelete==0:
                v1=arr[i]
            else:
                v1=prevonedelete+arr[i]
            onedelete=max(v1,prevnodelete)
            ans=max(ans,max(nodelete,onedelete))
        return ans
