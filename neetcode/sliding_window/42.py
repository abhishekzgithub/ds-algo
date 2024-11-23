"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

"""

class Solution(object):

    def area(self,height, l,r):
        return (r-l)* min(height[l], height[r])

    def brute_force(self,height):
        maxx_area=0
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                maxx_area=max(maxx_area, self.area(height,l,r))
        return maxx_area

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.brute_force(height)

height = [4,2,0,3,2,5]
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))