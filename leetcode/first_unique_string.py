"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        raw={}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=[i]
        print(seen)
        if len(seen.values())>1:
            return min(seen.values())[0]
        

s="loveleetcode" 
obj=Solution()
result = obj.firstUniqChar(s)
print(result)
