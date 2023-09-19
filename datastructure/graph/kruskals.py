"""
https://www.javatpoint.com/implementation-of-kruskals-algorithm-in-python
"""
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[]
        self.adjacency_list={v:[] for v in range(self.v)}
        self.parent=[]
        self.rank=[]
    
    def add_edge(self,u,v,weight):
        self.graph.append((u,v,weight))
        self.adjacency_list[u].append((v,weight))
        self.adjacency_list[v].append((u,weight))

    def find_parent(self,i,parent):
        if parent[i]==i:
            return i
        return self.find_parent(parent[i],parent)

    def do_union(self,parent,rank,u,v):
        root_u=self.find_parent(u,parent)
        root_v=self.find_parent(v,parent)
        # if rank is grater ,make it the parent
        if rank[root_v]>rank[root_u]: # 1>0=>1
            parent[root_u]=root_v
        elif rank[root_u]>rank[root_v]:
            parent[root_v]=root_u
        else:
            parent[root_v]=root_u
            rank[root_u]+=1
    
    def get_min_cost(self,result):
        mincost=0
        for u,v,w in result:
            mincost+=w
        print(mincost)
        return mincost

    def kruskals(self): # note: it doesn't required initial vertex unlike prims
        """
        step1: sort the graph based on weights
        """
        graph=sorted(self.graph,key=lambda x:x[2]) # weight soreted
        print(graph)
        result=[]
        for node in range(self.v):
            self.parent.append(node)
            self.rank.append(0) # ranking them all zeroes
        edge=0 # An index variable, used for result[]
        index=0 # An index variable, used for sorted edges
        while edge<self.v-1: # important: edge needs to be lopped completely.
            u,v,w=graph[index]
            x=self.find_parent(u,self.parent)
            y=self.find_parent(v,self.parent)
            if x!=y: # this to make sure they dont make loop
                edge+=1
                result.append(graph[index])
                self.do_union(self.parent,self.rank,u,v)
            index+=1
        print(result)
        return result

    def kruskals(self):
        graph=sorted(self.graph, key=lambda x: x[2])
        result=[]
        self.parent=[]
        self.rank=[]
        for ele in range(self.v):
            self.parent.append(ele)
            self.rank.append(0)
        edge=0
        index=0
        while edge<self.v-1:
            u,v,w=graph[index]
            parent_u=self.find_parent(u,self.parent)
            parent_v=self.find_parent(v,self.parent)
            if parent_u!=parent_v:
                edge+=1
                result.append(graph[index])
                self.do_union(self.parent,self.rank,u,v)
            index+=1
        print(result)
        return result
        

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    result = g.kruskals()
    g.get_min_cost(result)

