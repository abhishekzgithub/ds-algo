"""
https://www.geeksforgeeks.org/topological-sorting/
https://leetcode.com/problems/course-schedule/
check the editorial

"""

from collections import defaultdict
 
# Class to represent a graph
 
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.indegree_graph=defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree_graph[v].append(u)

    def _topological_sort(self,vertex,visited,stack):
        visited[vertex]=True
        nbrs=self.graph[vertex]
        for nbr in nbrs:
            if not visited[nbr]:
                self._topological_sort(nbr,visited,stack)
        stack.append(vertex) # note: important

    def topologicalSort(self):
        visited=[False]*self.V
        stack=[]
        for vx in range(self.V):
            print("vetex,neighbour",vx,self.graph[vx])
            if not visited[vx]:
                self._topological_sort(vx,visited,stack)
        print(stack[::-1]) #reversing it

    def is_cyclic(self):
        """
        things to note is we are correct on indegree definition
        we need to count the indegrees
        get the zero indegree so that it has some nbrs
        push it to the queue
        decrement the indegree so it isolates it
        append to Q if the decrement made it to zero
        check how many got pushed
        if its not equal to the total number of nodes, 
        then its a loop
        """
        indegree=defaultdict(lambda:0)
        queue=[]
        for u in self.indegree_graph:
            for v in self.indegree_graph[u]:
                indegree[u]+=1
        for ele in range(self.V):
            if indegree[ele]==0:
                queue.append(ele)
        count=0
        while queue:
            node=queue.pop()
            count+=1
            for nbr in self.graph[node]:
                print("nbr",nbr)
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    queue.append(nbr)
        print(count)
        return False if count==self.V else True
                
if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    #g.addEdge(3, 5)
 
    print("Following is a Topological Sort of the given graph")
 
    # Function Call
    #g.topologicalSort() #5 4 2 3 1 0 
    print(g.is_cyclic())