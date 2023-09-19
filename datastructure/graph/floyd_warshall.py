"""
this doesnt have visited=True
goes across all the nodes to relax

relaxes the weights by relaxing the node's weight by finding the intermediate or other ways to reach the destination node.
"""
import sys

class Graph:
    def __init__(self,graph) -> None:
        self.graph=graph
    
    def floyd_warshall(self):
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph)) # just trying to make deep copy of the graph
        print(dist)
        print(self.graph)
        V=len(self.graph)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]) # intermediate or other ways to reach the vertex
        print(dist)
        return dist
INF=sys.maxsize
graph = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0,   1],
            [INF, INF, INF, 0]
            ]
g=Graph(graph=graph)
g.floyd_warshall()