"""
kadane algorithm
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        step:
        loop over the elements and keep track of sum in total and max of sum
        if sum by any chance becomes negative, make it to zero.
        """
        maxx=nums[0]
        summ=0
        for ele in nums[:]:
            if summ<0:
                summ=0
            summ+=ele
            maxx=max(summ,maxx)
        return maxx

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8] #23
print(Solution().maxSubArray(nums))