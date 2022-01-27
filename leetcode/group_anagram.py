"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""


class Solution(object):
    @classmethod
    def _groupAnagrams(cls, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        HASH_DICT={}
        for ele in strs:
            xor_val=0
            for i in ele:
                xor_val^=ord(i)
            print(xor_val)
            print(HASH_DICT.values())
            if xor_val not in HASH_DICT:
                HASH_DICT[xor_val]=[ele]
            else:
                HASH_DICT[xor_val].append(ele)
        return HASH_DICT

    @classmethod
    def groupAnagrams(cls, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        HASH_DICT={}
        for ele in strs:
          
            sorted_val="".join(sorted(ele))
            print(sorted_val)
            if sorted_val not in HASH_DICT:
                HASH_DICT[sorted_val]=[ele]
            else:
                HASH_DICT[sorted_val].append(ele)
        return HASH_DICT.values()

strs=["eat","tea","tan","ate","nat","bat"]
output=[["bat"],["nat","tan"],["ate","eat","tea"]]
strs=["abbbbbbbbbbb","aaaaaaaaaaab"]
print(Solution.groupAnagrams(strs))