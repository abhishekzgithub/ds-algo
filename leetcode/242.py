"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sorted=sorted(s)
        t_sorted=sorted(t)
        if len(s_sorted)-len(t_sorted)!=0:
            return False
        else:
            for ele1,ele2 in zip(s_sorted, t_sorted):
                if ele1!=ele2:
                    return False
        return True

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sorted=sorted(s)
        t_sorted=sorted(t)
        if len(s_sorted)-len(t_sorted)!=0:
            return False
        else:
            for ele1,ele2 in zip(s_sorted, t_sorted):
                if ele1!=ele2:
                    return False
        return True

    def isAnagram(self, s, t):
        dict_s={}
        for ele in s:
            if dict_s.get(ele,None):
                dict_s[ele]+=1
            else:
                dict_s[ele]=1
        for ele in t:
            if dict_s.get(ele,None):
                dict_s[ele]-=1
            else:
                dict_s[ele]=1
        for ele in dict_s.values():
            if ele!=0:
                return False
        return True

s = "anagram"; t = "nagaram"
print(Solution().isAnagram(s,t)) #true