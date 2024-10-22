"""
https://leetcode.com/problems/contains-duplicate/
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited={}
        for ele in nums:
            if not visited.get(ele,None):
                visited[ele]=True
            else:
                return True
        return False

nums = [1,2,3,1]
nums = [1,2,3,4]
print(Solution().containsDuplicate(nums=nums))
        