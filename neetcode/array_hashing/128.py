"""
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

[0,3,7,2,5,8,4,6,0,1] ->9
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. keep finding the next element next to the current
        2. keep finding the prev element to the current
        3. keep a count of lce
        4. take a max of lce vs maxx for each
        """
        visited={i:False for i in nums}
        
        maxx=0
        for ele in nums:
            lce=1
            next_ele=ele+1
            while next_ele in visited and visited[next_ele]==False:
                lce+=1
                visited[next_ele]=True
                next_ele+=1
            prev_ele=ele-1
            while prev_ele in visited and visited[prev_ele]==False:
                lce+=1
                visited[prev_ele]=True
                prev_ele-=1
            maxx=max(maxx,lce)
            
        return maxx



nums = [100,4,200,1,3,2]
nums=[0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))