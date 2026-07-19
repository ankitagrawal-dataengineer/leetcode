class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero,one,res=0,0,0
        mp={}
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff == 0:
                res = max(res, i + 1)
            elif diff in mp:
                res = max(res, i - mp[diff])
            else:
                mp[diff] = i
        return res