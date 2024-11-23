"""
graph using the adjacency matrix
"""
from collections import defaultdict

class Vertex:
    def __init__(self, vertex):
        self.vertex=vertex
    
    def __str__(self):
        return str(self.vertex)

class Graph:
    def __init__(self):
        self.vertices={}

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
            element = stack.pop()
            #print("visiting {}".format(element))
            visited[element]=True #visit only when you pop
            nbrs = self.get_nbrs(element)
            for ele in nbrs:
                if not visited[ele]:
                    if ele not in stack:
                        stack.append(ele)
                    else:
                        print("{} in loop".format(ele))
                        return True

g=Graph()
g.add_weight({0,1},8)
#g.add_weight({0,1},8)
g.add_weight({1,2},8)
#g.add_weight({1,5},8)
g.add_weight({2,3},8)
g.add_weight({3,4},8)
g.add_weight({4,5},8)
g.add_weight({5,0})
g.add_weight({5,1})

#g()
#g.get_nbrs(5)
#g.bfs(0)
#g.dfs_recursive(0)
g.dfs(0)