class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, root):
        self.root=root

    def preorder(self, root):
        """
        right|root|left
        """
        if root is None:
            return root
        self.preorder(root.right)
        print(root.data)
        self.preorder(root.left)

    def search(self, root, node):
        """
        keep recursively return and searching till the end of the root
        once the root's next value is none or the value is equal to it, return that node
        """
        if root is None or root.data==node.data:
            #print(root, node)
            return node
        if node.data < root.data: # left
            return self.search(root.left, node)
        if root.data < node.data: #right
            return self.search(root.right, node)

    def insert(self, root, node):
        """
        check for the leftest or rightest node until you find the end of it.
        once you find the next node to be none, place the node at that place.
        """
        if root is None:
            return node
        if node.data < root.data: # left
            root.left=self.insert(root.left, node)
        if root.data < node.data: # right
            root.right=self.insert(root.right, node)
        return root

    def delete(self, root, node):
        """
        delete the node; complex # todo
        """
        if root is None:# or root.data==node.data:
            #print(root, node)
            return root
        if node.data < root.data: # left
            root.left = self.delete(root.left, node)
        elif root.data < node.data: #right
            root.right = self.delete(root.right, node)
        else:
            if root.left is None:
                temp=root.right
                root = None
                return temp
            if root.right is None:
                temp=root.left
                root = None
                return temp
        

A=Node(1)
B=Node(2)
C=Node(3)
D=Node(4)
E=Node(5)
F=Node(6)
# G=Node(7)
# H=Node(8)

bst = BinarySearchTree(A)
root = bst.insert(A, B)
root = bst.insert(root, C)
root = bst.insert(root, D)
root = bst.insert(root, E)
root = bst.insert(root, F)
#bst.preorder(A)
#print(bst.search(A,F))
#root = bst.delete(A,F)
bst.preorder(A)