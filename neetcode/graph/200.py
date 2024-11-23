"""
https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class Solution(object):
    def print_grid(self,grid):
        for row in grid:
            for item in row:
                print("|",end="\t")
                print(item, end='\t')
            print('\n')
        print("-"*80)

    def check_boundary(self,grid,row,col):
        if 0<=row<len(grid) and 0<=col<len(grid[0]):
            return True
        return False

    def visit_nbr(self,queue, grid,direction):
        while queue:
            row, col = queue.pop(0)
            for xy in direction:
                new_row=row+xy[0]
                new_col=col+xy[1]
                if self.check_boundary(grid,new_row,new_col) and grid[new_row][new_col]=="1":
                    queue.append((new_row,new_col))
                    grid[new_row][new_col]="0"

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        direction=[(-1,0),(0,1),(0,-1),(1,0)]
        island_count=0
        queue=[]
        #self.print_grid(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #print(grid[row][col])
                if grid[row][col]=="1":
                    queue.append((row,col))
                    grid[row][col]="0"
                    
                    self.visit_nbr(queue,grid,direction)
                    island_count+=1
                    self.print_grid(grid)
        return island_count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] #3
print(Solution().numIslands(grid))