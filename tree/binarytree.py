class Node:
    def __init__(self, data):
        self.right=None
        self.left=None
        self.data = data

    def __str__(self):
        return "Node:"+str(self.data)

class BinarySearchTree:
    """
    pre-requisites are it only works with digits or values which we can compare with.
    https://www.programiz.com/dsa/binary-search-tree
    """
    root = None
    def __init__(self):
        self.root=None

    def inorder(self, node):
        """
        LRR : Left root right
        """
        if not node:
            return node
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
 
    def preorder(self, node):
        """
        RtLR : root Left right
        """
        if not node:
            return node
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        """
        LRR : Left  right root
        """
        if not node:
            return node
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
        return None

    def add(self, root, node):
        if root==None:
            return node
        if node.data < root.data:
            root.left = self.add(root.left,node)
        elif node.data > root.data:
            root.right = self.add(root.right,node)
        return root

    def search(self, root, node):
        print(root)
        if not root or root.data==node.data:
            return root
        if node.data < root.data:
            self.search(root.left, node)
        elif node.data > root.data:
            self.search(root.right, node)

btree = BinarySearchTree()
root = btree.root
root = btree.add(root, Node(4))
#print(root)
root =btree.add(root, Node(2))
#print(root.left)
root =btree.add(root, Node(5))
#print(root.right)

root =btree.add(root, Node(1))
root =btree.add(root, Node(3))
btree.preorder(root)
#btree.inorder(root)
#btree.postorder(root)

#print(btree.search(root,Node(1)))