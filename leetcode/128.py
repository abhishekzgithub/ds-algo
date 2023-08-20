"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest, s = 0, set(nums)
        for num in nums:
            cur_longest, j = 1, 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest, j = cur_longest + 1, j + 1
            j = 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest, j = cur_longest + 1, j + 1
            longest = max(longest, cur_longest)
        return longest
    
    def longestConsecutive(self, nums):
        nums_set=set(nums)
        j=1
        longest=0
        curr_longest=0
        for n in nums:
            if (n-j) in nums_set:
                while (n-j) in nums_set:
                    nums_set.remove(n-j)
                    curr_longest+=1
                    j+=1
            j=1
            if (n+j) in nums_set:
                while (n+j) in nums_set:
                    nums_set.remove(n+j)
                    curr_longest+=1
                    j+=1
                    
            longest=max(longest,curr_longest)
        return longest

    def longestConsecutive(self, nums):
        numset=set(nums)
        longest=0
        for n in nums:
            if (n-1) not in numset:
                curr_longest=0
                while (n+curr_longest) in numset:
                    curr_longest+=1
                longest=max(longest,curr_longest)
        return longest



nums=[100,4,200,2,3,1]
print(Solution().longestConsecutive(nums))
            