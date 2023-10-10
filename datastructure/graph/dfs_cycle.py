from collections import defaultdict

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