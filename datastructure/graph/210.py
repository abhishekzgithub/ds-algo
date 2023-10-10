"""
https://leetcode.com/problems/course-schedule-ii/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

"""
from collections import defaultdict

class Solution(object):

    def _topological_sorting(self,ix,visited,stack,adj_graph):
        visited.append(ix)
        for nbr in adj_graph[ix]:
            if nbr not in visited:
                self._topological_sorting(nbr,visited,stack,adj_graph)
        stack.append(ix)

    def topological_sorting(self,numCourses,prerequisites):
        visited=[]
        stack=[]
        adj_graph=defaultdict(list)
        for u,v in prerequisites:
            adj_graph[u].append(v)
        for ix in range(numCourses):
            if ix not in visited:
                self._topological_sorting(ix,visited,stack,adj_graph)
        return stack [::]

class Graph:
    def __init__(self,vertices,graph):
        self.vertices=vertices
        self.graph=defaultdict(list)
        for u,v in graph:
            self.graph[u].append(v)

    def _dfs(self,node,visited,res):
        """
        It returns false whenever it finds a visited node
        """
        if visited[node]==-1: # unvisited
            return False
        if visited[node]==1: #visited
            return True
        visited[node]=-1
        for nbr in self.graph[node]:
            if not self._dfs(nbr,visited,res):
                return False
        #if there is a loop it wont reach here
        visited[node]=1
        res.append(node)
        return True

    def dfs(self,vertex=None,visited=None,res=None):
        visited = [0 for _ in range(self.vertices)] # initial
        res=[]
        for node in range((self.vertices)):
            if not self._dfs(node,visited,res): #loop detection
                return []
        return res


vertex=[[1,0],[2,0],[3,1],[3,2]]
vertices = 4

print(Graph(vertices,vertex).dfs())
vertex=[[0,1],[1,0]]
vertices = 2

print(Graph(vertices,vertex).dfs())

# numCourses = 4; prerequisites = [[1,0],[2,0],[3,1],[3,2]] #[0,2,1,3] or [0,1,2,3]
# print(Solution().findOrder(numCourses,prerequisites))
# #print(Solution().topological_sorting(numCourses,prerequisites))
# print("-"*5)
# numCourses = 1; prerequisites = [] #[0]
# print(Solution().findOrder(numCourses,prerequisites))
# #print(Solution().topological_sorting(numCourses,prerequisites))
# print("-"*5)
# numCourses = 2; prerequisites = [[1,0]] #[0,1]
# print(Solution().findOrder(numCourses,prerequisites))
# #print(Solution().topological_sorting(numCourses,prerequisites))
# print("-"*5)
# numCourses = 2; prerequisites =[[0,1],[1,0]] #[]
# print(Solution().findOrder(numCourses,prerequisites))
# #print(Solution().topological_sorting(numCourses,prerequisites))
