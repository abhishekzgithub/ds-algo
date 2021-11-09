#https://leetcode.com/problems/sort-colors/
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects 
of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""
class Solution(object):
    def _sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        this is a bubble sort implementation
        """
        for i in range(0,len(nums)-1):
            for j in range(1, len(nums)-i):
                if nums[j-1]>nums[j]:
                    nums[j-1], nums[j] = nums[j],nums[j-1]
        return nums

    def sortColors(self, nums):
        red,white,blue=0,0,len(nums)-1
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==0:

                pass
            elif nums[l]==2:
                pass
            


nums=[2,0,2,1,1,0]
print(Solution().sortColors(nums))
#print(Solution().(nums))