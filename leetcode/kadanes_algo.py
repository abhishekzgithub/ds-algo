# https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far=nums[0]
        max_ending_here=nums[0]
        list_array=nums
        for i in range(1,len(list_array)):
            max_ending_here = max(list_array[i], list_array[i]+max_ending_here)
            max_so_far=max(max_so_far, max_ending_here)
            # max_ending_here = max_ending_here+list_array[i]
            # if max_ending_here<0: #once it reaches to zero , start again
            #     max_ending_here=0
            # if max_ending_here>max_so_far:
            #     max_so_far=max_ending_here
            print(max_ending_here, max_so_far)
        return max_so_far