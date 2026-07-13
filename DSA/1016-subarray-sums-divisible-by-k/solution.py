class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums=0
        d=dict()
        d[0]=1
        res=0
        for i in range(len(nums)):
            sums+=nums[i]
            rem=sums%k
            if rem<0:
                rem+=k
            res+=d.get(rem,0)
            d[rem]=d.get(rem,0)+1
        return res