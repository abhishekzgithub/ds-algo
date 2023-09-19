"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        #todo: incomplete
        :type s: str
        :type k: int
        :rtype: int
        """
        l,r,curr_k=0,0,0
        freq_dict={}
        max_length=0
        s=list(s)
        #freq_dict[s[l]]=freq_dict.get(s[l],0)+1
        while r<len(s):
            freq_dict[s[r]]=freq_dict.get(s[r],0)+1
            if s[l]==s[r] and curr_k<=k:
                max_length=max(max_length,(r-l+1))
            elif s[l]!=s[r] and curr_k<=k:
                #s[r]=max(freq_dict,key=freq_dict.get)
                max_length=max(max_length,(r-l+1))
                curr_k+=1
            r+=1
        return max_length,s

s="AABABBA";k=1 #4

# s="ABAB";k=2
# s="AAAA";k=0 #4

print(Solution().characterReplacement(s,k)) #4