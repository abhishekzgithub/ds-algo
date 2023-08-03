"""
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
"""

class Solution:
    def getConcatenation(self, nums):
        news_nums=[-1]*2*len(nums)
        print(news_nums)
        for index in range(len(nums)):
            news_nums[index],news_nums[index+len(nums)]=nums[index],nums[index]
        return news_nums

    def getConcatenation(self, nums):
        news_nums=[-1]*2*len(nums)
        print(news_nums)
        for index in range(len(nums)):
            news_nums[index],news_nums[index+len(nums)]=nums[index],nums[index]
        return news_nums

nums = [1,2,1]
print(Solution().getConcatenation(nums))