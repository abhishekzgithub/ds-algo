class Graph:
    def __init__(self, size) -> None:
        self.size=size
        self.adj_edge=[[] for i in range(self.size)]
    
    def add_edge(self,s,e):
        self.adj_edge[s].append(e)
        self.adj_edge[e].append(s)
    
    def _dfs_rec(self,node, visited):
        visited[node]=True
        print("visited",node)
        for i in self.adj_edge[node]:
            if not visited[i]:
                self._dfs_rec(i,visited)
    
    def dfs_disconnected(self):
        visited=[False]*len(self.adj_edge)

        for v in range(len(self.adj_edge)):
            if not visited[v]:
                self._dfs_rec(v,visited)

    def dfs(self):
        visited=[False]*len(self.adj_edge)
        self._dfs_rec(1,visited)
    
    def bfs(self):
        from collections import deque
        #q=[0]
        #while len(q)!=0:




if __name__ == "__main__":
    V = 6  # Number of vertices
    graph = Graph(V)

    # Define the edges of the graph
    edges = [(1, 2), (2, 0), (0, 3), (4, 5)]

    # Populate the adjacency list with edges
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    print("Complete DFS of the graph:")
    graph.dfs()  # Perform DFS