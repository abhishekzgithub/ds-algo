from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while len(queue)>0:
            print(queue)
            node=queue.pop(0)
            for nbr in self.graph[node]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr]=True # it has visited

    def dfs(self,s):
        """Here we dont mark the node as visited
            while checking for neighbours.
            We mark them while popping it out.
        """
        visited=defaultdict(lambda :False)
        stack=[]
        stack.append(s)
        while len(stack)>0:
            print(stack)
            node=stack.pop()
            if not visited[node]:
                visited[node]=True
            for nbr in self.graph[node]:
                if not visited[nbr]:
                    stack.append(nbr) # yet to visit

    def dfs_recursive(self,s,visited):
        stack=[]
        stack.append(s)
        while len(stack):
            print(stack, end=" ")
            node=stack.pop()
            if node not in visited:
                visited.add(node)
            for nbr in self.graph[node]:
                if nbr not in visited:
                    self.dfs_recursive(nbr,visited)

    def dfs_recursive(self,v,visited):
        visited.add(v)
        print(v, end=' ')
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_recursive(neighbour, visited)

if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 4)

    g.bfs(0)
    print("-"*10)
    g.dfs(0)
    print("-"*10)
    g.dfs_recursive(0,set())