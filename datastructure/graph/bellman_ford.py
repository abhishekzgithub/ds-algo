"""
https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
No visited=True appraoch
No positive or negative edge side effect
Run over n-1 vertices to relax the graph
Run again and see if any change is present, then its a loop.
"""
import sys

class Graph:
    def __init__(self,v):
        self.vertices=v
        self.graph=[]
    
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def bellman_ford(self,src):
        # stp_set=[False]*self.vertices # no visting approach here
        dist=[sys.maxsize]*self.vertices
        dist[src]=0
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.vertices-1): # note: only n-1 vertices are relaxed
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u,v,w in self.graph:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for u,v,w in self.graph:
            if dist[v]>dist[u]+w:
                return "Loop or negative loop"
        
        return dist

g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

# function call
print(g.bellman_ford(0)) #[0, -1, 2, -2, 1]
