"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
"""

class Solution(object):
    brackets_keys = {')':'(', '}':'{',']':'['}
    
    def isValid(self,s):
            brackets_keys={'(':')', '{':'}','[':']'}
            stack = []
            for i in s:
                if i in brackets_keys:  # 1
                    stack.append(i)
                elif len(stack) == 0 or brackets_keys[stack.pop()] != i:  # 2
                    return False
            return len(stack) == 0 # 3

    def isValid(self,s):
        brackets_keys=self.brackets_keys
        stack=[]
        for ele in s:
            if ele not in brackets_keys:
                  stack.append(ele)
            else:
                if len(stack)!=0 and brackets_keys[ele]==stack[-1]:
                      stack.pop()
                else:
                    return False
        return len(stack)==0



s="[]()"
s="]"
print(Solution().isValid(s))
