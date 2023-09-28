"""
https://leetcode.com/problems/number-of-islands/description/
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

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
    
    def is_safe(self,x,y,matrix):
        if (0<=x<len(matrix) and 0<=y<len(matrix[0])):
            return True
        return False

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        lands=[]
        island=0
        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col]=="1":
                    lands.append((row,col))
        print(lands)
        for land in lands:
            queue=[]
            queue.append(land)
            while queue:
                #print(queue)
                x,y=queue.pop(0)
                visited.add((x,y))
                for dx,dy in directions:
                    new_x=x+dx
                    new_y=y+dy
                    if self.is_safe(new_x,new_y,grid) and grid[new_x][new_y]=="1" and (new_x,new_y) not in visited:
                        queue.append((new_x,new_y))
                        visited.add((new_x,new_y))
                        lands.remove((new_x,new_y))
            island+=1
            
        return island
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=[]
        island=0
        def _numIslands(queue):
            while queue:
                x,y=queue.pop(0)
                for dx,dy in directions:
                    new_x=x+dx
                    new_y=y+dy
                    if self.is_safe(new_x,new_y,grid) and grid[new_x][new_y]=="1":
                        queue.append((new_x,new_y))
                        grid[new_x][new_y]="0"
    
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col]=="1":
                    grid[row][col]=="0"
                    queue.append((row,col))
                    _numIslands(queue)
                    island+=1
        return island

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] #1
_grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] # 3
print(Solution().numIslands(grid)) #1
