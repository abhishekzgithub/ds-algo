"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"


"""

class Solution(object):

    def check_palindrome(self, pal_str,res):
        i=0
        j=len(pal_str)-1
        while i<j//2:
            if pal_str[i]!=pal_str[j]:
                res[pal_str]=False
                return res
            i+=1
            j-=1
        res[pal_str]=True
        return res
        

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res={}
        hash_max={ele:ix for ix, ele in enumerate(s)}
        for ix in range(len(s)):
            max_ix=hash_max[s[ix]]
            if ix<max_ix:
                res=self.check_palindrome(s[ix:max_ix+1], res)
            elif ix==max_ix:
                pass
        return res.keys()#[0] if res else None
            

s="babad"
s="aba"
#print(Solution().longestPalindrome(s))
print(Solution().longestPalindrome(s))