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
    """
    this is a dutch national flag problem.
    get the low, mid and high
    check for mid.(important)
    if mid is 0, swap with low and increment low
    if mid is 2, swap with high and decrement high
    else increment mid
    """

    def sortColors(self, nums):
        l,m,h=0,0,len(nums)-1
        while m<=h:
            if (nums[m]==0):
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif (nums[m]==2):
                nums[h],nums[m]=nums[m],nums[h]
                h-=1
            else:
                m+=1

    def sortColors(self, nums):
        red,white,blue=0,0,len(nums)-1
        while red<=blue:
            if nums[white]==0:
                nums[red],nums[white]=nums[white], nums[red]
                red+=1
                white+=1
            elif nums[white]==2:
                nums[white],nums[blue]=nums[blue], nums[white]
                blue-=1
            else:
                white+=1
            


nums=[2,0,2,1,1,0]
print(Solution().sortColors(nums))
#print(Solution().(nums))