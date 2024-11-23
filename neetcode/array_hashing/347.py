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
    def brute_solution(self,nums,k):
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

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for ele in nums:
            freq[ele]=freq.get(ele,0)+1
        bucket=[[] for i in range(len(nums)+1)]
        print(bucket, freq)
        for n,c in freq.items():
            bucket[c].append(n)
        res=[]
        print(bucket)
        for index in range(len(bucket)-1, 0,-1):
            print(index)
            if bucket[index]:
                for ele in bucket[index]:
                    res.append(ele)
        return res[:k]

nums = [1,1,1,2,2,3,4]; k = 4
#nums=[-1,-1];k=1
print(Solution().topKFrequent(nums,k))