"""
The logic behind is of set theory {ele1, ele2}, First find the first element which is supposed to be lower
and then the second element in the range of closing side of set.
"""

import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sub_ele=[sys.maxsize,sys.maxsize]
        for ele in nums:
            if ele<sub_ele[0]:
                sub_ele[0]=ele
            elif ele>sub_ele[0] and ele<sub_ele[1]:
                sub_ele[1]=ele
            elif ele>sub_ele[1]:
                return True
        return False

nums=[1,2,3,4,5]
sol=Solution()
print(sol.increasingTriplet(nums))