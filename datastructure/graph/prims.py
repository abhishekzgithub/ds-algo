class Graph:
    def __init__(self,v):
        self.vertices=v
        self.graph=[]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def fn_minimum_vertex(self, visited_set,key):
        mini=float("INF")
        for v in range(self.vertices):
            if key[v]<mini and visited_set[v]==False:
                mini=key[v]
                mini_index=v
        return mini_index

    def prims(self,s):
        mst_visited=[False]*self.vertices
        key=[float("INF")]*self.vertices
        parent=[None]*self.vertices
        key[0]=0
        parent[0]=-1 # this -1 indicates root values
        for _  in range(self.vertices):
            minimum_source_vertex=self.fn_minimum_vertex(mst_visited,key)
            mst_visited[minimum_source_vertex]=True
            for vertex in range(self.vertices):
                if self.graph[minimum_source_vertex][vertex]>0\
                    and mst_visited[vertex]==False \
                    and key[vertex]>self.graph[minimum_source_vertex][vertex]:
                    
                    key[vertex]=self.graph[minimum_source_vertex][vertex]
                    parent[vertex]=minimum_source_vertex
        
        return self.printMST(parent)






if __name__=="__main__":
    g=Graph(4)
    g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
    print(g.prims(0))