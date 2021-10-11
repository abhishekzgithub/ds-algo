"""
assumption
the root will always be smaller than all the elements below it
operation involved:
insert()
delete()
getmin()
extractmin()
decreasekey()

heap will be complete binary tree following the given formulae:
parent: (i-1)/2
root: n-1/2
left: (2*i)+1
right: (2*i)+2

notes:
the insertion happens at the end i.e. at the leaf and heapify happens wrt parent
you should delete only the root.
if deleted, the last element will take the place of root and then heapify.
The hole play is about the index
max heap
            30
        20       7
    9     15  4      8
"""

class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None

class MinHeap:
    def __init__(self):
        self.root=None
        self.heap = []
        self.max_cap = 3
    def parent(self, index):
        return index//2

    def left(self, index):
        return (2*index)+1

    def right(self, index):
        return (2*index)+2

    def insert(self,node):
        if len(self.heap)==self.max_cap:
            return
        if len(self.heap)!=0:
            self.heap.append(node)
        self.heapify()
        # if not root:
        #     return
        # if node.data<root.data:
        #     root.left=node
        # if node.data>root.data:
        #     root.right=node
        # return root

    def delete(self, node):
        pass

    def heapify(self):
        pass # todo

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

A1 = Node(1)
A2 = Node(2)
A3 = Node(3)
A4 = Node(4)
A5 = Node(5)

minheap = MinHeap()
minheap.root = A2
root = minheap.insert(minheap.root,A1)
root = minheap.insert(root, A3)
root = minheap.insert(root, A4)
root = minheap.insert(root, A5)
minheap.inorder(root)