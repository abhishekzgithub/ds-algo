"""
graph using the prims algorithm
pre-requisites:
all vertex has to be connected and weighted
"""
from collections import defaultdict
import sys
class Vertex:
    def __init__(self, vertex):
        self.vertex=vertex
    
    def __str__(self):
        return str(self.vertex)

class Graph:
    def __init__(self):
        self.vertices={}
        self.visited = defaultdict(lambda : False)

    def __call__(self):
        for key, val in self.vertices.items():
            print("Vertex {} has neighbours as {}".format(key, val))

    def add_edge(self, edge):
        src_node , dest_node = edge
        if src_node not in self.vertices:
            self.vertices[src_node] = set()
        if dest_node not in self.vertices:
            self.vertices[dest_node] = set()
        if not self.vertices[src_node]:
            self.vertices[src_node]={dest_node}
        else:
            self.vertices[src_node].update({dest_node})
        if not self.vertices[dest_node]:
            self.vertices[dest_node]={src_node}
        else:
            self.vertices[dest_node].update({src_node})

    def add_weight(self, edge, weight=1):
        """
        just add a tuple (dest_node, weight) to the vertices src_node list
        """
        src_node , dest_node = edge
        if src_node not in self.vertices:
            self.vertices[src_node] = []
        if dest_node not in self.vertices:
            self.vertices[dest_node] = []
        if not self.vertices[src_node]:
            self.vertices[src_node]=[(dest_node, weight)]
        elif (dest_node, weight) in self.vertices[src_node]:
            pass
        else:
            self.vertices[src_node].extend([(dest_node, weight)])
        if not self.vertices[dest_node]:
            self.vertices[dest_node]=[(src_node, weight)]
        elif (src_node, weight) in self.vertices[dest_node]:
            pass
        else:
            self.vertices[dest_node].extend([(src_node, weight)])
    def get_nbrs(self, src_node):
        nbr = []
        for key, value in self.vertices.items():
            if key==src_node and self.vertices[key]:
                for item in self.vertices[key]:
                    nbr.append(item[0])
                break
        print("Source node {} neighbours are {}".format(src_node, nbr))
        return nbr

    def bfs(self, src_node):
        """
        visit the first node
        get nbrs
        append it to the queue
        pop first
        mark as visited
        get the nbrs
        append it to the queue
        """
        from collections import defaultdict
        q=[]
        visited = defaultdict(lambda :False)
        q.append(src_node)
        #visited[src_node]=True
        while len(q)>0:
            #print(visited)
            element = q.pop(0) #visit only when you pop
            print("visiting {}".format(element))
            visited[element]=True
            nbrs = self.get_nbrs(element)
            for ele in nbrs:
                if not visited[ele]:
                    if ele not in q:
                        q.append(ele) #adding at the end of the queue
                    else:
                        print("{} in loop".format(ele))
                        return True

    def dfs_recursive(self, src_node, visited=defaultdict(lambda :False)):
        """
        dfs will recursively check for the visited nodes in the neibours
        """
        visited[src_node]=True
        print("visted {}".format(src_node))
        nbrs = self.get_nbrs(src_node)
        for ele in nbrs:
            if not visited[ele]:
                self.dfs_recursive(ele, visited)

    def dfs(self, src_node):
        from collections import defaultdict
        stack=[]
        visited = defaultdict(lambda :False)
        stack.append(src_node)
        #visited[src_node]=True
        while len(stack)>0:
            #print(visited)
            element = stack.pop(0)
            #print("visiting {}".format(element))
            visited[element]=True #visit only when you pop
            nbrs = self.get_nbrs(element)
            for ele in nbrs:
                if not visited[ele]:
                    if ele not in stack:
                        stack.insert(0,ele) #adding on top of stack
                    else:
                        print("{} in loop".format(ele))
                        return True
    
    def get_least_weight_nbr(self, src_node, visited):
        nbr = self.vertices[src_node]#self.get_nbrs(src_node)
        least_weight = sys.maxsize
        print("src_node {} nbr{}".format(src_node,nbr))
        nbr_vertex = None 
        for ele in nbr:
            if ele[1]<least_weight and ele[0] not in visited:
                nbr_vertex, least_weight = ele
        return nbr_vertex, least_weight

    def prims(self, source_node):
        visited = defaultdict(lambda : False)
        while self.vertices.get(source_node,None) and source_node not in visited:
            visited[source_node]=True
            nbr_vertex, least_weight = self.get_least_weight_nbr(source_node, visited)
            print("Source node:{} Nbrvertex:{} Leastweight: {}".format(source_node,nbr_vertex, least_weight))
            source_node = nbr_vertex

    def prims_recursive(self, source_node, visited=None):
        if source_node is None:
            return
        self.visited[source_node]=True
        nbr_vertex, least_weight = self.get_least_weight_nbr(source_node, self.visited)
        return self.prims_recursive(nbr_vertex, self.visited)

g=Graph()
g.add_weight({0,1},2)
g.add_weight({0,3},1)
#g.add_weight({0,5},1)
g.add_weight({1,2},2)
#g.add_weight({1,5},8)
g.add_weight({2,3},3)
g.add_weight({3,4},4)
g.add_weight({4,5},5)
g.add_weight({5,0},8)
#g.add_weight({5,1})

#g()
#g.get_nbrs(5)
#g.bfs(0)
#g.dfs_recursive(0)
#g.dfs(0)
#g.prims(0)
g.prims_recursive(0)