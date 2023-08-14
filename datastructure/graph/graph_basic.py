"""
graph using the adjacency matrix
"""
class Node:
    def __init__(self, node):
        self.node=node

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_matrix=[]
        for _ in range(self.nodes):
            self.adj_matrix.append([0 for i in range(self.nodes)])

    def print_graph(self):
         for arr in range(len(self.adj_matrix)):
            print(self.adj_matrix[arr])

    def add_nbr(self, src_node, dest_node):
        self.adj_matrix[src_node][dest_node]=1

    def get_nbrs(self, src_node):
        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[src_node][i]==1:
                print("Connected nodes of {} are {}".format(src_node,i))





g=Graph(3)
g.add_nbr(0,1)
g.add_nbr(0,2)
g.add_nbr(1,2)
g.add_nbr(1,0)
g.add_nbr(2,0)
g.print_graph()
g.get_nbrs(0)
g.get_nbrs(1)
