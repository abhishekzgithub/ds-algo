"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        make the product shift one at a time to the right and store it in 'm' and then save it in prefix temp list
        make the product shift one at a time to the left and store it in 'm' and then save it in postfix temp list
        at the end just multiply all the indexes
        """
        temp_left=[1]*(len(nums))
        m=1
        for ele in range(1,len(nums)):
            temp_left[ele]=nums[ele-1]*m
            m=temp_left[ele]
        temp_right=[1]*(len(nums))
        m=1
        for ele in range(1,len(nums)):
            temp_right[-ele-1]=nums[-ele]*m
            m=temp_right[-ele-1]
        for ix in range(len(nums)):
            nums[ix]=temp_left[ix]*temp_right[ix]
        return nums


    def _productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
nums=[1,2,3,4]
obj=Solution()
print(obj.productExceptSelf(nums))