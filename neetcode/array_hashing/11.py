"""
https://leetcode.com/problems/container-with-most-water/
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
class Solution(object):

    def area(self,height,l,r):
        return (r-l)*min(height[l],height[r])
    
    def brute_force(self, height):
        maxx=0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area=(r-l)*min(height[l],height[r])
                maxx=max(maxx,area)
        return maxx

    def optimized(self, height):
        l,r=0,len(height)-1
        maxx_area=0
        while l<r:
            maxx_area=max(maxx_area, self.area(height,l,r))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxx_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #return self.brute_force(height)
        return self.optimized(height)
        


height=[1,8,6,2,5,4,8,3,7] #49
print(Solution().maxArea(height))