"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Input: s = "()[]{}"

Output: true
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        open_bracket="[{("
        for ele in s:
            print(ele)
            if ele in open_bracket:
                stack.append(ele)
            else:
                if stack and ( (ele==")" and stack[-1]=="(") or (ele=="]" and stack[-1]=="[") or (ele=="}" and stack[-1]=="{")):
                    stack.pop()
                else:
                    return False
        return len(stack)==0
        

s="()[]{}"
#s="(]"
#s="["
print(Solution().isValid(s))