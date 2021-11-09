"""
https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]


[-4, -1, -1, 0, 1, 2]
"""

class Solution:

    def get_target(self, nums_array, target):
        l,r=0, len(nums_array)-1

        while l<r:
            sum_nums=nums_array[l]+nums_array[r]
            if sum_nums>target:
                r-=1
            elif sum_nums<target:
                l+=1
            else:
                return [nums_array[l],nums_array[r]]
        return None

    def threeSum(self, nums):
        sorted_nums=sorted(nums)
        print(sorted_nums)
        final_result=[]
        for index, val in enumerate(sorted_nums):
            if val==sorted_nums[index-1] and index>0:
                continue
            print(val)
            result=(self.get_target(sorted_nums[:], -val))
            if result:
                result.append(val)
                final_result.append(result)
        return final_result
        
nums=[-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))