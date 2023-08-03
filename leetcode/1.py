"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        recIndex={}
        for index, ele in enumerate(nums):
            diff = target - ele
            if diff in recIndex:
                return [recIndex[diff],index]
            else:
                recIndex[ele]=index
        return

nums=[7,2,11,15]
target=9
#nums=[3,2,4]
#target=6
print(Solution().twoSum(nums,target))