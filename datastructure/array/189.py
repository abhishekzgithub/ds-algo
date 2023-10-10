"""
https://leetcode.com/problems/rotate-array/description/
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
def rotate(nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		queue=nums[::]
		for ix in range(k):
			temp=queue.pop()
			queue.insert(0,temp)
		return queue
def rotate(nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		for ix in range(k):
			tempp=nums[-1]
			nums=[tempp]+nums[:len(nums)-1]
		return nums

def rotate(nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		n=len(nums)
		if k>n:
			  k=k%n
		reverserd_nums=sorted(nums,reverse=True) # reverse 
		reverserd_nums1=sorted(reverserd_nums[0:k],reverse=False) #sort
		reverserd_nums2=sorted(reverserd_nums[k:n],reverse=False)
		return reverserd_nums1+reverserd_nums2

def rotate(nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		n=len(nums)
		if k>n:
			k=k%n
		nums=nums[::-1]
		nums=nums[0:k][::-1]+nums[k:n][::-1]
		return nums

def rotate(nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		def reverse_num(arr):
			return arr[::-1]
		n=len(nums)
		if k>n:
			k=k%n
		nums=reverse_num(nums)
		nums=reverse_num(nums[0:k])+reverse_num(nums[k:n])
		return nums

def rotate(nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.

		Step 1: Reverse the last k elements of the array

		Step 2: Reverse the first n-k elements of the array.

		Step 3: Reverse the whole array.
		"""
		def reverse_num(arr,i,j):
			while i<j:
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
				i+=1
				j-=1
			return arr
		n=len(nums)
		if k>n:
			k=k%n
		nums=reverse_num(nums,0,n-k-1)
		nums=reverse_num(nums,n-k,n-1)
		nums=reverse_num(nums,0,n-1)
		return nums

nums = [1,2,3,4,5,6,7]; 
k = 3 #[5,6,7,1,2,3,4] 
#k = 7 #[1,2,3,4,5,6,7]
#k=8 #[7, 1, 2, 3, 4, 5, 6]
k=9 #[6, 7, 1, 2, 3, 4, 5]
#k=63 #[1, 2, 3, 4, 5, 6, 7] #7%63 is 0 so no rotation required
print(rotate(nums,k))