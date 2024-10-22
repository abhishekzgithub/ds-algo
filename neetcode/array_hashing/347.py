"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

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
            if not freq.get(ele,None):
                freq[ele]=1
            else:
                freq[ele]+=1
        print(freq)
        keys=[]
        for key,val in freq.items():
            if val>=k:
                keys.append(key)

        return (keys)

nums = [1,1,1,2,2,3]; k = 2
print(Solution().topKFrequent(nums,k))