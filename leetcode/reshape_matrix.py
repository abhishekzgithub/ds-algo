"""
https://leetcode.com/problems/reshape-the-matrix/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

"""

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)*len(mat[0])!=r*c:
            return mat
        matrix_ele=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                matrix_ele.append(mat[i][j])
        y=0
        new_mat=[]
        for i in range(r):
            new_mat.append([])
            for j in range(c):
                new_mat[y].append(matrix_ele.pop(0))
            y+=1
        return new_mat

mat = [[1,2,6],[3,4,7]] 
r = 1
c = 6
r=2
c=4
obj=Solution()
result=obj.matrixReshape(mat, r,c)
print(result)
