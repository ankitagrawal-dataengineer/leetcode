class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        sums=0
        d=dict()
        d[0]=1
        for i in range(len(nums)):
            sums+=nums[i]
            ques=sums-k
            count+=d.get(ques,0)
            d[sums]=d.get(sums,0)+1
        return count


