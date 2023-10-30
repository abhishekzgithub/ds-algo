"""
[12:11 PM] Mitul Verma

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"

Output: true

Example 2:

Input: s = "abcde", goal = "abced"

Output: false

[12:11 PM] Mitul Verma

class Solution:

    def rotateString(self, s: str, goal: str) -> bool:

"""
class Solution:

    def rotateString(self, s, goal):
        i=0
        last=len(s)-1
        temp_s=""
        while i<len(s):
            temp_s=s[0]
            s=s[1:len(s)]+temp_s
            i+=1
            if s==goal:
                return True
        return False

s="abcde"
goal="abced"
print(Solution().rotateString(s,goal))
s = "abcde"; goal = "cdeab"
print(Solution().rotateString(s,goal))
