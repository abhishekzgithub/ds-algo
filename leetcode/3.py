"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_dict={}
        start=0
        max_length=0
        for i in range(len(s)):
            if s[i] in hash_dict and start<=hash_dict[s[i]]:
                start=hash_dict[s[i]]+1
            else:
                max_length=max(max_length, i-start+1)
            hash_dict[s[i]]=i
        return max_length
    def _lengthOfLongestSubstring(self, s):
        """
        very slow
        """
        i=0
        stack=[]
        max_length=0
        while i<len(s):
            if s[i] not in stack:
                stack.append(s[i])
                max_length=max(max_length, len(stack))
                i+=1
            else:
                stack=[]
                s=s[1:]
                i=0
        return max_length

s="aabcbb"
sol=Solution()
print(sol.lengthOfLongestSubstring(s))