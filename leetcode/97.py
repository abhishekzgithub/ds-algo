# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        n_list=[]
        return self.inorder(root,n_list)
    
    def inorder(self, root, node_list):
        if not root:
            return
        self.inorder(root.left, node_list)
        node_list.append(root.val)
        self.inorder(root.right, node_list)
        return node_list
        