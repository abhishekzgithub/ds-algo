"""
https://leetcode.com/problems/permutation-in-string/description/
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        NOTE: permutation way of doing it
        """
        def permute(string_val,state,result):
            if not string_val:
                result.append("".join(state))
                return
            
            for idx in range(len(string_val)):
                state.append(string_val[idx])
                permute(string_val[:idx]+string_val[idx+1:],state,result)
                state.pop()
        state=[]
        result=[]
        self.permute(s1,state,result)
        for ele in result:
            if ele in s2:
                return True
        return False

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        sliding window approach
        """
        def get_sorted(val):
            return "".join(sorted(val)) #O(klogk) * O(k) * O(K)
        s1_sorted=get_sorted(s1)
        window_length=len(s1)
        i=0
        j=i+window_length
        while j<=len(s2):
            print(s2[i:j])
            if s1_sorted==get_sorted(s2[i:j]):
                return True
            i+=1
            j=i+window_length
        return False

if __name__=="__main__":
    s1 = "ab"; s2 = "eidboaoo" #false
    s1 = "ab"; s2 = "eidbaooo" #True
    s1="dinitrophenylhydrazine";s2="acetylphenylhydrazine" #false
    #s1="adc";s2="dcda" #True
    obj=Solution()
    print(obj.checkInclusion(s1,s2))