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
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                diff=abs(s-target)
                if max_diff>diff:
                    max_diff=diff
                    res_sum=s
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    return s
        return res_sum