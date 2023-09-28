"""
https://leetcode.com/problems/rotting-oranges/description/
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

994. Rotting Oranges
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

class Solution(object):

    def _orangesRotting(self,state,grid,col,row,result,index,visited):

        # if col==len(grid) and row==len(grid):
        #     return True
        if col<0 or col>=len(grid):
            return False
        if row<0 or row>=len(grid):
            return False
        if grid[col][row]==0:
            return False
        # if grid[col][row]==1:
        #     return True
        if (col,row) in visited:
            return False
        
        visited.append((col,row))
        res=(
            self._orangesRotting(state,grid,col-1,row,result,index,visited) #top
            or self._orangesRotting(state,grid,col+1,row,result,index,visited) #bottom
            or self._orangesRotting(state,grid,col,row-1,result,index,visited) #left
            or self._orangesRotting(state,grid,col,row+1,result,index,visited) #right
        )
        print(res)
        #print(res)
        #print(visited)
        visited.pop()#remove((col,row))
        #print(result)
        return res


    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        state=[]
        result=[]
        index=0
        visited=[(0,0)]
        counter=0
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if self._orangesRotting(state,grid,col,row,result,index,visited):
                    counter+=1
                    return True
        return counter

class Solution2(object):
    def bfs(self,grid,col,row,fresh_orange_count,rotten_orange):
        pass

    def orangesRotting(self,grid):
        rotten_orange=[]
        time=0
        fresh_orange_count=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row]==1:
                    fresh_orange_count.add((col,row))
                if grid[col][row]==2:
                    rotten_orange.append((col,row,time))
        while rotten_orange :
            col,row,time=rotten_orange.pop(0)
            for dirc in directions:
                dc,dr=dirc
                if (0<=(col+dc) <=len(grid)-1
                    and 0<=(row+dr)<=len(grid[0])-1
                    and grid[col+dc][row+dr]==1
                    and (col+dc,row+dr) in fresh_orange_count
                    ):
                    grid[col+dc][row+dr]=2
                    rotten_orange.append((col+dc,row+dr,time+1))
                    fresh_orange_count.remove((col+dc,row+dr))
        return time if not fresh_orange_count else -1
        

    def _orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        fresh_set=set()
        rotten = []
        step = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y]==1:
                    fresh_set.add((x,y))
                elif grid[x][y]==2:
                    rotten.append([x,y,step])
        while rotten:
            x,y,step = rotten.pop(0)
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy] == 1:
                    grid[x+dx][y+dy]=2
                    fresh_set.remove((x+dx,y+dy))
                    rotten.append([x+dx,y+dy,step+1])#note: tricky mind of step
        return step if not fresh_set else -1


class _Solution:
    def orangesRotting(self, grid):#: List[List[int]]) -> int:
        fresh_visit, rotten = set(), deque()
		# find all fresh and rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_visit.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        result = 0
        while fresh_visit and rotten:
			# BFS iteration
            for _ in range(len(rotten)): #for every pop
                i, j = rotten.popleft()  # obtain recent rotten orange
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in fresh_visit:  # check if adjacent orange is fresh
                        fresh_visit.remove(coord)
                        rotten.append(coord)
            result += 1
		# check if fresh oranges remain and return accordingly
        return -1 if fresh_visit else result

grid = [[2,1,1],[1,1,0],[0,1,1]] #4
print(Solution2().orangesRotting(grid))
grid=[[2,1,1],[0,1,1],[1,0,1]] #-1
print(Solution2().orangesRotting(grid))
grid=[[0,2]] #0
print(Solution2().orangesRotting(grid))
grid=[[0]] #0

print(Solution2().orangesRotting(grid))


# visited.append((col,row))
        # if self._orangesRotting(state,grid,col-1,row,result,index,visited):
        #     result.append((col,row))
        #     return True
        # if self._orangesRotting(state,grid,col+1,row,result,index,visited):
        #     result.append((col,row))
        #     return True
        # if self._orangesRotting(state,grid,col,row-1,result,index,visited):
        #     result.append((col,row))
        #     return True
        # if self._orangesRotting(state,grid,col,row+1,result,index,visited):
        #     result.append((col,row))
        #     return True
        #visited.pop()