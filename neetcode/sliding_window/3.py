"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        maxx=0
        size=0
        hash_dict={}
        while j<len(s):
            print(hash_dict,s[j],j,maxx,i,s[i])
            if s[j] in hash_dict:
                i=max(i,hash_dict[s[j]]+1) #things to notice, the index has to be greater than i and less than j
            size=j-i+1
            maxx=max(size, maxx)
            hash_dict[s[j]]=j
            j+=1
        return maxx

    def __lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int abcabcbb
        """
        if len(s) == 0:
            return 0
        seen = {}
        left, right = 0, 0
        longest = 1
        while right < len(s):
            if s[right] in seen:
                left = max(left,seen[s[right]]+1)
            longest = max(longest, right - left + 1)
            seen[s[right]] = right
            right += 1
            print(left, right, longest)
        return longest

s= "abcabcbb" #3
s = "bbbbb"
s="abba" #2
s="dvdf"
print(Solution().lengthOfLongestSubstring(s))