class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d=dict()
        d[0]=1
        count,s=0,0
        for i in range(len(nums)):
            s+=nums[i]
            ques=s-k
            count+=d.get(ques,0)
            d[s]=d.get(s,0)+1
        return count