"""
graph using the adjacency matrix
"""
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
    

g=Graph()
g.add_weight({0,1},8)
g.add_weight({1,2},8)
g.add_weight({1,3},8)
g.add_weight({1,3},8)
g.add_weight({3,4})
g.add_weight({4,5})
g()
