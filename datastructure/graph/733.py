"""
https://leetcode.com/problems/flood-fill/description/
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
"""

class Solution(object):

    def is_safe(self,x,y,matrix):
        if (0<=x<len(matrix) and 0<=y<len(matrix[0])):
            return True
        return False

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        queue=[]
        visited=set()
        source_color=image[sr][sc]
        print(source_color)
        queue.append((sr,sc))
        direction=[(0,1),(0,-1), (1,0), (-1,0),(0,0)]
        while queue:
            row,col=queue.pop(0)
            for row_ix,col_ix in direction:
                if (self.is_safe(row+row_ix,col+col_ix,image)
                    and image[row+row_ix][col+col_ix]==source_color
                and (row+row_ix,col+col_ix) not in visited):
                    queue.append((row+row_ix,col+col_ix))
                    visited.add((row+row_ix,col+col_ix))
                    image[row+row_ix][col+col_ix]=color
                    #print(image)
        return image



image = [[1,1,1],[1,1,0],[1,0,1]]; sr = 1; sc = 1; color = 2
print(Solution().floodFill(image,sr,sc,color))
#[[2,2,2],[2,2,0],[2,0,1]]

image=[[0,0,0],[0,0,0]]
sr=1
sc=0
color=2
## [[2,2,2],[2,2,2]]
print(Solution().floodFill(image,sr,sc,color))

image=[[0,0,0],[0,1,0]];sr=1;sc=1;color=2 #[[0,0,0],[0,2,0]]
print(Solution().floodFill(image,sr,sc,color))