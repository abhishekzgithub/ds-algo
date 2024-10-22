"""
https://leetcode.com/problems/valid-anagram/
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram_dict={}
        if len(s)<len(t): # this is done to reverse the operation
            s,t=t,s
        for ele in s:
            print(ele)
            if not anagram_dict.get(ele,None):
                anagram_dict[ele]=1
            else:
                anagram_dict[ele]+=1

        for ele in t:
            if not anagram_dict.get(ele,None):
                anagram_dict[ele]=1
            else:
                anagram_dict[ele]-=1

        for key, val in anagram_dict.items():
            if val!=0:
                return False
        return True

s="rat"
s="rac"
t="car"
s="a"
t="abb"
print(Solution().isAnagram(s,t))