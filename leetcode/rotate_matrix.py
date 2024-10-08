#https://leetcode.com/problems/rotate-image/
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2,3],\
                 [4,5,6],
                 [7,8,9]]
Output: [[7,4,1],
         [8,5,2],
         [9,6,3]]

"""

class Solution(object):
    
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i]=temp
        #print(matrix)
        matrix = self.swap(matrix)
        return(matrix)
    
    def swap(self, matrix):
        n = len(matrix)-1
        mid=n//2
        for i in range(0,n+1):
            for j in range(0, mid+1):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][n-j]
                matrix[i][n-j]=temp
                print(matrix)
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

output = (Solution().rotate(matrix))
print(output)
#assert output==[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
