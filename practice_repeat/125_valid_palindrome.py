import re
class Solution(object):


    def _helper(self,array_chars):
        start=0
        end=len(array_chars)-1
        while start<=end:
            if array_chars[start]==array_chars[end]:
                start+=1
                end-=1
            else:
                return False

        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #re.match(r"[a-zA-Z0-9]",ele)
        s_lower=s.lower()
        print(s)
        sample=""
        for ele in s_lower:
            if re.match(r"[a-zA-Z0-9]",ele):
                sample+=ele.lower()
        return self._helper(sample)
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome

s="A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))