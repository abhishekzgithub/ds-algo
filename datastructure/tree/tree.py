class Node:
    def __init__(self, data):
        self.right=None
        self.left=None
        self.data = data

    def __str__(self):
        return "Node:"+self.data

class Tree:
    """
    Binary tree is all about traversal such as inorder, preorder,postorder.
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

tree = Tree()

A= Node("A")
tree.root = A
B= Node("B")
C= Node("C")
D= Node("D")
E= Node("E")

A.left=B
A.right=C
B.left=D
B.right=E
print(tree.postorder(tree.root))
