# Definition for a binary tree node.
class Node(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):

    def __init__(self):
        self.root=None

    def insert(self,root,node):
        if isinstance(node,Node):
            if node.data < root.data:
                if root.left is None:
                   root.left=node
                else:
                    self.insert(root.left,node)
            elif node.data > root.data:
                if root.right is None:
                   root.right=node
                else:
                    self.insert(root.right,node)
        return

    def inorder(self,root):
        if root:
            (self.inorder(root.left))
            print(root.data)
            (self.inorder(root.right))

class Solution(object):
    def maxDepth(self, root, count=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        #root = [3,9,20,None,None,15,7]
        if root:
            count=count+1+max(self.maxDepth(root.left, count),self.maxDepth(root.right, count))
        else:
            count= 0
        return count
A0=Node(3)
A=Node(9)
B=Node(20)
C=Node(1)
D=Node(2)
E=Node(15)
F=Node(7)

bst=BinarySearchTree()
root=bst.root=A0
bst.insert(root,A)
bst.insert(root,B)
bst.insert(root,C)
bst.insert(root,D)
bst.insert(root,E)
bst.insert(root,F)
#bst.inorder(root)
obj=Solution()
print(obj.maxDepth(root)==4) # returns 4 as ans