"""
Kadane's algorithm

https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2 loops; 1 loop for outer
        and 2nd inner loop from outer index to the end
        """
        max_sum=0
        ssum=0
        for x in range(len(nums)):
            ssum=0
            for y in range(x,len(nums)):
                ssum+=nums[y]
                max_sum=max(max_sum,ssum)
            print(max_sum)
        return max_sum

    def maxSubArray(self, nums):
        """
        two conditions:
        1. if sum till now is zero, reset the sum to zero
        2. at every sum, get the max sum.
        """
        n=len(nums)
        max_sum=nums[0]
        ssum=0
        for ix in range(n):
            if ssum<0:
                ssum=0
            ssum+=nums[ix]
            max_sum=max(max_sum,ssum)
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums=[-1]
print(Solution().maxSubArray(nums))