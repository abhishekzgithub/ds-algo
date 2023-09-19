"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/#:~:text=A%20province%20is%20a%20group,the%20total%20number%20of%20provinces.
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

class Solution(object):

    def find_parent(self,x,parent):
        if parent[x]==x:
            return parent[x]
        return self.find_parent(parent[x],parent)

    def do_union(self,parent,rank,x,y):
        x=self.find_parent(x,parent)
        y=self.find_parent(y,parent)
        if rank[x]>rank[y]:
            parent[y]=x
        elif rank[y]>rank[x]:
            parent[x]=y
        else:
            parent[y]=x
            rank[x]+=1
        return (parent,rank)
    def _findCircleNum(self,matrix):
        """
        union find approach
        """
        parent=[]
        rank=[]
        connected=len(matrix)
        for ele in range(len(matrix)):
            parent.append(ele)
            rank.append(0)
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                if matrix[x][y]==1 and self.find_parent(x,parent)!=self.find_parent(y,parent):
                    connected-=1
                    parent, rank = self.do_union(parent,rank,x,y)
        return connected

    def bfs(self, node,visited,matrix):
        queue=[]
        queue.append(node)
        visited[node]=True
        while len(queue)>0:
            first_node=queue.pop(0)
            for row in range(len(matrix)):
                if visited[row]==False and matrix[first_node][row]==1:
                    queue.append(row)
                    visited[row]=True
                    

    def findCircleNum(self,matrix):
        """
        bfs approach
        """
        visited=[False]*len(matrix)
        print(visited)
        connected=0
        for node in range(len(matrix)): #column
            if visited[node]==False:
                connected+=1
                self.bfs(node,visited,matrix) 
        return connected


isConnected = [[1,1,0],[1,1,0],[0,0,1]] #2
isConnected=[[1,0,0],[0,1,0],[0,0,1]] # 3
isConnected=[[1,1,1],[1,1,1],[1,1,1]] #1
s=Solution()
print(s.findCircleNum(isConnected))