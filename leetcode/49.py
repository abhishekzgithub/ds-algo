"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution(object):
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
    
    def _groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        main_output=[]
        for ele in range(len(strs)):
            output=[]
            for next_ele in range(ele,len(strs)):
                if self.isAnagram(strs[ele],strs[next_ele]):
                    if strs[next_ele] not in output:
                        output.append(strs[next_ele])
            main_output.append(output)
        return main_output
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table=dict()
        for ele in strs:
            sorted_ele="".join(sorted(ele))
            print(sorted_ele,ele)
            if hash_table.get(sorted_ele,None):
                hash_table[sorted_ele].append(ele)
            else:
                hash_table[sorted_ele]=[ele]
        return list(hash_table.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))