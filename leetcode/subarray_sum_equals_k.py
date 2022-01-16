"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of "continuous subarrays" whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2
"""

class Solution(object):
    def _subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        The problem is to find out how many subsets can be made to find the target k. 
        I used the longest subarray method to do it.
        """
        counter=0
        for ix in range(len(nums)):
            m=0
            target=0
            for ele in range(ix, len(nums)):
                target=nums[ele]+m
                m=target
                if m==k:
                    counter+=1
                    print(-ix+ele+1)
        return counter

    def subarraySum(self, nums, k):
        from collections import defaultdict
        m=0
        target=0
        total=0
        hash_table=defaultdict(lambda : 0)
        for ix in range(len(nums)):
            m+=nums[ix]
            target = m-k
            if target in hash_table:
                total+=hash_table[target]
            if m==k:
                total+=1
            hash_table[m]+=1
        return (hash_table),total

nums=[1,1,1]
k=2
nums=[1,2,3]
k=3
oout=2
# nums=[1,2,1,2,1]
# k=3

obj=Solution()
print(obj.subarraySum(nums, k))