class Graph:
    def __init__(self, v) -> None:
        self.adj=[[] for i in range(v)]
        self.visited=[False]*v

    def add_edge(self,node1,node2):
        self.adj[node1].append(node2)
        self.adj[node2].append(node1)
    
    def _dfs_recur(self,visited,i):
        visited[i]=True
        print(i)
        for nbr in self.adj[i]:
            if not visited[nbr]:
                self._dfs_recur(visited,nbr)

    def dfs(self):
        visited=[False] * len(self.adj)
        for i in range(len(self.adj)):
            if not visited[i]:
                self._dfs_recur(visited,i)

    def dfs_iter(self, src_node):
        visited=[False] * len(self.adj)
        stack=[]
        stack.append(src_node)
        visited[src_node]=True
        while len(stack)>0:
            start_node=stack.pop()
            print(start_node)
            visited[start_node]=True
            nbrs=self.adj[start_node]
            for nbr in nbrs:
                if not visited[nbr]:
                    stack.append(nbr)

    def dfs_iter_loop(self, src_node):
        visited=[False] * len(self.adj)
        stack=[]
        stack.append(src_node)
        visited[src_node]=True
        while len(stack)>0:
            start_node=stack.pop()
            print(start_node)
            visited[start_node]=True
            nbrs=self.adj[start_node]
            for nbr in nbrs:
                if not visited[nbr]:
                    if nbr in stack:
                        print(f"{start_node} is the loop")
                        return True
                    stack.append(nbr)

    def bfs_iter(self,src_node):
        visited=[False] * len(self.adj)
        queue=[]
        queue.append(src_node)
        while len(queue)!=0:
            start_node=queue.pop(0)
            print(start_node)
            visited[start_node]=True
            nbrs=self.adj[start_node]
            for nbr in nbrs:
                if not visited[nbr]:
                    queue.append(nbr)


    def bfs_iter_loop(self,src_node):
        visited=[False] * len(self.adj)
        queue=[]
        queue.append(src_node)
        while len(queue)!=0:
            start_node=queue.pop(0)
            print(start_node)
            visited[start_node]=True
            nbrs=self.adj[start_node]
            for nbr in nbrs:
                if not visited[nbr]:
                    if nbr not in queue:
                        queue.append(nbr)
                    else:
                        print(f"{start_node} is the loop")
                        return True


print(Graph(6).adj)
g=Graph(6)
edges = [(1, 2), (2, 0), (0, 3), (3,4),(4, 5),(5,0)]
for ele in edges:
    g.add_edge(ele[0],ele[1])

print(g.adj)
print(g.dfs(),end="\n\n")
print(g.dfs_iter(0),end="\n\n")
print(g.bfs_iter(0),end="\n\n")
print(g.bfs_iter_loop(0),end="\n\n")
print(g.dfs_iter_loop(0),end="\n\n")