"""
https://leetcode.com/problems/invert-binary-tree/description/
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Input: root = [2,1,3]
Output: [2,3,1]
"""
from binary_tree import BinaryTree
class Solution(BinaryTree):
    def invertTree(self, root,node_list):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root,node_list):
            if not root:
                return None
            temp=root.left
            root.left=root.right
            root.right=temp
            dfs(root.left,node_list)
            dfs(root.right,node_list)
            return root
        return dfs(root,node_list)

if __name__=="__main__":
    root = [2,1,3] #[2,3,1]
    root = [4,2,7,1,3,6,9] #[4,7,2,9,6,3,1]
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    print(bt.preorder(bt.root,"root",bt.root))
    node_list=[]
    bt.root=bt.invertTree(bt.root,node_list)
    print(node_list)
    print(bt.preorder(bt.root,"root",bt.root))