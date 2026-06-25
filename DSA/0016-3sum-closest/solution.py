class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        max_diff=float('inf')
        res_sum=0
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                diff=abs(s-target)
                if diff<max_diff:
                    max_diff=diff
                    res_sum=s
                elif s==target:
                    return res_sum
                elif s<target:
                    left+=1
                else:
                    right-=1
        return res_sum
