#https://leetcode.com/problems/3sum/
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

class Solution:

    def two_sum_two(self, nums, target, resultant):
        l,r =0, len(nums)-1
        while l<r:
            total=nums[l]+nums[r]+target
            if total>0:
                r-=1
            elif total<0:
                l+=1
            else:
                resultant.add((target, nums[l], nums[r]))
                l+=1

    def threeSum(self, nums):
        nums=sorted(nums)
        print(nums)
        resultant=set()
        for index, num in enumerate(nums):
            if index>0 and num==nums[index-1]:
                continue
            result=self.two_sum_two(nums[index+1:], num, resultant)
        return (resultant)
    

    def threeSumPart1(self, nums):
        nums.sort()
        added = set()
        out = []
        for i in range(len(nums) - 1, -1, -1):
            last = nums[i]
            start, end = 0, i - 1
            while start < end:
                s = last + nums[start] + nums[end]
                if s == 0:
                    if (last, nums[start], nums[end]) not in added: out.append([last, nums[start], nums[end]])
                    added.add((last, nums[start], nums[end]))
                    start += 1
                elif s > 0:
                    end -= 1
                else: start += 1
        return out

nums=[-1,0,1,2,-1,-4]
nums=[-4, -1, -1, 0, 1, 2]
print(Solution().threeSum(nums))
        