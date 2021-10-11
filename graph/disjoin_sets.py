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
        self.parent = defaultdict(lambda : -1)
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

    def get_weight(self, src_node, dest_node):
        weight=None
        for node, nbr in self.vertices.items():
            #print(node, nbr)
            if node==src_node:
                for ele in nbr:
                    if ele[0]==dest_node:
                        weight=ele[1]
                        return weight

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
    
    def sort_weight(self):
        weight_list=[]
        node_list=list(self.vertices.keys())
        for node_index in range(0,len(node_list)-1):
            node=node_list[node_index]
            nbr=node_list[node_index+1]
            weight=self.get_weight(node, nbr)
            if weight:
                weight_list.append({weight:(node,nbr)})
        return weight_list

    def union(self, parent, x,y):
        x_set=self.find_parent(parent,x)
        y_set=self.find_parent(parent,y)
        parent[y_set]=x_set

    def find_parent(self, parent, node):
        if parent[node]==-1:
            return node
        else:
            self.find_parent(parent, parent[node])

    def find_cycle(self, source_vertex):
        nbrs = self.vertices[source_vertex]
        print(nbrs)
        
        #sorted_weight = self.sort_weight()
        #print(sorted_weight)
        # for key, value in self.vertices.items():
        #     print(key, value)

g=Graph()
g.add_weight({0,1},10)
#g.add_weight({0,1},8)
g.add_weight({1,2},20)
#g.add_weight({1,5},8)
g.add_weight({2,3},30)
g.add_weight({3,4},40)
g.add_weight({4,5},50)
#g.add_weight({5,0})
#g.add_weight({5,1})

#g()
#g.get_nbrs(5)
#g.bfs(0)
#g.dfs_recursive(0)
#g.dfs(0)
g.find_cycle(0)