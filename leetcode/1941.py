"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
"""

class Solution:
    def areOccurrencesEqual(self, s):
        place_dict={}
        for ele in s:
            if place_dict.get(ele,None):
                place_dict[ele]+=1
            else:
                place_dict[ele]=1
        if max(place_dict.values())==min(place_dict.values()):
            return True
        return False





s="abacbca"
print(Solution().areOccurrencesEqual(s))