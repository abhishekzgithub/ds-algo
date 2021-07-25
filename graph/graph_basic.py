"""
graph using the adjacency matrix
"""

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_matrix=[]
        for i in range(nodes):
            self.adj_matrix.append([0 for i in range(nodes)])
       
    def print_graph(self):
         for arr in range(len(self.adj_matrix)):
            print(self.adj_matrix[arr])

    def add_nbr(self, src_node, dest_node):
        self.adj_matrix[src_node][dest_node]=1
 
g=Graph(3)
g.add_nbr(0,1)
g.add_nbr(1,2)
g.add_nbr(2,0)
g.print_graph()