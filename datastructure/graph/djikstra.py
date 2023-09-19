import sys

class Graph:
    def __init__(self,vertices) -> None:
        self.v=vertices
        self.graph=[[0 for col in range(self.v) for row in range(self.v)]]
    
    def min_distance(self,dist,spt_set):
        min=sys.maxsize
        min_index=None
        for destination in range(self.v):
            if dist[destination]<min and spt_set[destination]==False:# find minimum distance and not visited
                min=dist[destination]
                min_index=destination
        return min_index

    def dijkstra(self,src):
        dist=[sys.maxsize] * self.v # mark all the vertices as infinity
        spt_set=[False]* self.v # shortest path traversed set as false
        dist[src]=0 # mark the first one as zero
        for source in range(self.v):
            min_index=self.min_distance(dist,spt_set)
            spt_set[min_index]=True
            for destination in range(self.v):
                if self.graph[source][destination]>0 \
                    and spt_set[destination]==False \
                    and dist[destination]>dist[source]+self.graph[source][destination]:
                    dist[destination]=dist[source]+self.graph[source][destination] #relaxing the distance
        print(dist)
    
    def dijkstra(self,src):
        dist=[sys.maxsize]*self.v
        spt_set=[False]*self.v
        dist[src]=0
        for source in range(self.v):
            min_index=self.min_distance(dist,spt_set)
            spt_set[min_index]=True
            for dest in range(self.v):
                if dist[dest]>dist[source]+self.graph[source][dest] \
                    and spt_set[dest]==False \
                    and self.graph[source][dest]>0:
                    dist[dest]=dist[source]+self.graph[source][dest]
        print(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]
g.dijkstra(0)