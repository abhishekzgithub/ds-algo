"""
https://leetcode.com/problems/contains-duplicate/
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        resultant={}
        for ele in nums:
            if ele in resultant:
                return True
            else:
                resultant[ele]=0


nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))