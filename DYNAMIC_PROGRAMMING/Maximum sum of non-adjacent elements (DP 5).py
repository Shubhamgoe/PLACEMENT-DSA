# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        dpf = [0 for i in range(n)]
        dpf[0] = nums[0]
        dpf[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dpf[i] = max(nums[i]+dpf[i-2],dpf[i-1])
        return dpf[(len(nums)-1)]
        

        