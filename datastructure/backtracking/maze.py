"""
https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
1.find the stop criteria/condition/result
2.put the data through the criteria/condition/move along thing:dfs will take care of it
3.if not found a certain criteria to move forward, unset the value
"""

matrix=[[1,0,0,0,0],
        [1,1,0,0,0],
        [0,1,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,1]]

class Maze:
    def __init__(self,maze_matrix) -> None:
        self.maze_matrix=maze_matrix
        self.X=len(self.maze_matrix)
        self.Y=len(self.maze_matrix[0])
        self.solution_maze_matrix=[[0 for x in range(self.X) ] for y in range(self.Y)]

    def is_safe(self, current_x,current_y,maze_matrix):
        if (current_x>=0 and current_x<=self.X-1
            and current_y>=0 and current_y<=self.Y-1
            and maze_matrix[current_x][current_y]==1
            ):
            return True
        return False
    
    def has_reached_end(self,current_x, current_y,maze_matrix):
        if (current_x>=0 and current_x<=self.X-1
            and current_y>=0 and current_y<=self.Y-1
            and current_x==self.X-1 and current_y==self.Y-1
            and maze_matrix[current_x][current_y]==1
            
            ):
            return True
        return False

    def maze(self,x,y,maze_matrix,solution_maze):

        if self.has_reached_end(x,y,maze_matrix):
            solution_maze[x][y]==1
            return True

        if self.is_safe(x,y,maze_matrix):
            if solution_maze[x][y]==1:
                return False
            solution_maze[x][y]=1
            if self.maze(x+1,y,maze_matrix,solution_maze):
                return True
            if self.maze(x-1,y,maze_matrix,solution_maze):
                return True
            if self.maze(x,y+1,maze_matrix,solution_maze):
                return True
            if self.maze(x,y-1,maze_matrix,solution_maze):
                return True
            solution_maze[x][y]=0
        return False

    def maze_util(self):
        initial_x=0
        initial_y=0
        maze_matrix=self.maze_matrix
        solution_maze_matrix=self.solution_maze_matrix
        
        status= self.maze(initial_x,initial_y,maze_matrix,solution_maze_matrix)
        return status

print(Maze(matrix).maze_util())