"""
https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        m=1
        for ix in range(1,len(nums)):
            prefix[ix]=nums[ix-1]*m
            m=prefix[ix]
        m=1
        for ix in range(1,len(nums)):
            postfix[-ix-1]=nums[-ix]*m
            m=postfix[-ix-1]
        for index in range(len(nums)):
            nums[index]=prefix[index]*postfix[index]
        return nums

nums=[1,2,3,4]
print(Solution().productExceptSelf(nums))