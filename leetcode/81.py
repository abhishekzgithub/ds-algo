"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
81. Search in Rotated Sorted Array II
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

"""
def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: bool
	"""
	low=0
	high=len(nums)-1
	while low<=high:
		while low<high and nums[low]==nums[low+1]:
			low=low+1
		while low<high and nums[high-1]==nums[high]:
			high-=1
		mid=(low+high)//2
		if nums[mid]==target:
			return True
		elif nums[low]<=nums[mid]:
			if nums[low]<=target<=nums[mid]:
				high=mid-1
			else:
				low=mid+1
		elif nums[mid]<=nums[high]:
			if nums[mid]<=target<=nums[high]:
				low=mid+1
			else:
				high=mid-1
	return False
		

nums= [2,5,6,0,0,1,2]; target = 3 #false
print(search(nums,target))
nums = [2,5,6,0,0,1,2]; target = 0 #true
print(search(nums,target))
nums=[1,0,1,1,1];target=0 #true
print(search(nums,target))
nums=[1,3];target=3 #true
print(search(nums,target))