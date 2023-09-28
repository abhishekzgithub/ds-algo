"""
https://leetcode.com/problems/course-schedule/description/
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
class Solution(object):

    def find_parent(self,x,parent):
        if x==parent[x]:
            return parent[x]
        return self.find_parent(parent[x],parent)
    
    def do_union(self,x,y,rank,parent):
        parent_x=self.find_parent(x,parent)
        parent_y=self.find_parent(y,parent)
        if parent_x==parent_y:
            return
        if rank[parent_x]>rank[parent_y]:
            parent[parent_y]=parent_x
        elif rank[parent_y]>rank[parent_x]:
            parent[parent_x]=parent_y
        else:
            parent[parent_y]=parent_x
            rank[parent_x]+=1
    

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        rank=[]
        parent={}
        loop=False

        for ix in range(numCourses):
            parent[ix]=ix
            rank.append(0)

        for x,y in prerequisites:
            if self.find_parent(x,parent)==self.find_parent(y,parent):
                loop=True
                print("coords",x,y)                
            else:
                self.do_union(x,y,rank,parent)
            print(rank[x],rank[y])
        return not loop
    
from collections import defaultdict
 
# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def _topological_sort(self,vertex,visited,stack):
        visited[vertex]=True
        nbrs=self.graph[vertex]
        for nbr in nbrs:
            if not visited[nbr]:
                self._topological_sort(nbr,visited,stack)
        stack.append(vertex) # note: important

    def topologicalSort(self):
        visited=[False]*self.V
        stack=[]
        for vx in range(self.V):
            print("vetex,neighbour",vx,self.graph[vx])
            if not visited[vx]:
                self._topological_sort(vx,visited,stack)
        print(stack[::-1]) #reversing it

class Solution:
    def canFinish(self, numCourses, prerequisites):
        __doc__="""
            this is Kahn's algorithm
            things to note is we are correct on indegree definition
            we need to count the indegrees A-->B (B has one indegree)
            get the zero indegree so that it has some nbrs
            push it to the queue
            decrement the indegree so it isolates it
            append to Q if the decrement made it to zero
            check how many got pushed
            if its not equal to the total number of nodes, 
            then its a loop
            """
        graph=defaultdict(list)
        indegree=defaultdict(lambda :0)
        for u,v in prerequisites:
            graph[v].append(u) #take a note here
            indegree[u]+=1
        # print(graph)
        # print("indegree")
        # print(indegree)
        queue=[]
        for ele in range(numCourses):
            if indegree[ele]==0:
                queue.append(ele)
        count=0
        while queue:
            node =queue.pop()
            count+=1
            for nbr in graph[node]:
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    queue.append(nbr)
        #print("Indegree now",indegree)
        return count==numCourses

class Solution:
    def dfs(self, node, adj, visit, inStack):
        # If the node is already in the stack, we have a cycle.
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # Mark the current node as visited and part of current recursion stack.
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        # Remove the node from the stack.
        inStack[node] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        time complexity=O(M+N)
        """
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True

numCourses = 2
prerequisites = [[1,0]] #true
print(Solution().canFinish(numCourses,prerequisites))
print("\t\t")
prerequisites=[[1,0],[0,1]] #false
print(Solution().canFinish(numCourses,prerequisites))
print("\t\t")
numCourses=5 #special case
g=Graph(numCourses)
prerequisites=[[1,4],[2,4],[3,1],[3,2]] #true
print(Solution().canFinish(numCourses,prerequisites))
# for u,v in prerequisites:
#     print(g.addEdge(u,v))

# g.topologicalSort()
