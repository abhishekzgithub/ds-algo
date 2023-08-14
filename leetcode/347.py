"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for ele in nums:
            freq[ele]=1+freq.get(ele,0)
        return freq

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums,k))