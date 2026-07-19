class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d=dict()
        d[0],s,res=1,0,0
        for i in range(len(nums)):
            s+=nums[i]
            rem=s%k
            if rem<0:
                rem+=k
            res+=d.get(rem,0)
            d[rem]=d.get(rem,0)+1
        return res