"""
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
        """
        l,h=0,1
        maxx=0
        while h<=len(nums)-1:
            if nums[l]+nums[h]<0:
                l+=1
            else:
                maxx=max(maxx,nums[l]+nums[h])
            h+=1
        return maxx

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))