"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                mid=high-1
            else:
                return mid
        return -1


nums=[-1,0,3,5,9,12]
target=9
print(Solution().search(nums,target))