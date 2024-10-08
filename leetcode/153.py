"""
153. Find Minimum in Rotated Sorted Array
Medium
11.4K
510
Companies
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=len(nums)-1
        
        while i<j:
            mid=(i+j)//2 # focus on mid element
            if nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid
        return nums[i] # return the mininum

nums=[1,2,3,4,5]
print(Solution().findMin(nums))
nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums))
nums = [3,4,5,1,2]
print(Solution().findMin(nums))

nums = [4,5,6,7,8,0,1,2]
print(Solution().findMin(nums))