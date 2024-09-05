"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_list=defaultdict(list)
        for ele in strs:
            print(sorted(ele))
            sorted_ele="".join(sorted(ele))
            if sorted_ele not in group_list:
                group_list[sorted_ele]=[ele]
            else:
                group_list[sorted_ele].append(ele)

        return group_list.values()



strs= ["eat","tea","tan","ate","nat","bat"]
output=[["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().groupAnagrams(strs))
        