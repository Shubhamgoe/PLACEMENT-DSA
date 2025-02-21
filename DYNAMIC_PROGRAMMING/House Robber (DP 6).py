# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(max(nums[0],nums[1]),nums[2])
        first = nums[:n-1]
        second = nums[1:]
        dpf = [0 for i in range(n-1)]
        dps = [0 for i in range(n-1)]
        dpf[0] = first[0]
        dpf[1] = max(first[0],first[1])
        for i in range(2,len(first)):
            dpf[i] = max(first[i]+dpf[i-2],dpf[i-1])
        dps[0] = second[0]
        dps[1] = max(second[0],second[1])
        for i in range(2,len(second)):
            dps[i] = max(second[i]+dps[i-2],dps[i-1])
        
        return max(dpf[(len(first)-1)],dps[(len(second)-1)])