"""
https://leetcode.com/problems/subtree-of-another-tree/description/
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
    def _isSubtree(self, root, sub_root):
        """
        this is to find same tree
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def _dfs(root,sub_root):
            if root==None and sub_root==None:
                return True
            if root==None or sub_root==None:
                return False
            return(
                (root.val==sub_root.val)
                and _dfs(root.left,sub_root.left)
                and _dfs(root.right,sub_root.right)
            )
        return _dfs(root,sub_root)

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot: return True
        if not root: return False

        def bfs(root,sub_root):
            queue=[root]
            while queue:
                node =queue.pop()
                if node.val==sub_root.val:
                    if self._isSubtree(node,sub_root):
                        return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return False
        return bfs(root,subRoot)
    
    def isSubtree(self,root,subRoot):
        if not root:
            return False
        if not subRoot:
            return True
        def is_same_tree(p,q):
            if p and q:
                return (p==q 
                        and is_same_tree(p.left,q.left) 
                        and is_same_tree(p.right,q.left))
            return p is q
        if is_same_tree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) 
                or self.isSubtree(root.right,subRoot))


if __name__=="__main__":
    root = [3,4,5,1,2]; subRoot = [4,1,2] #true
    root = [3,4,5,1,2,None,None,None,None,0]; subRoot = [4,1,2] #false
    bt,bt_subroot=Solution(), Solution()
    bt.root=bt.preorder_insert(root)
    bt_subroot.root=bt_subroot.preorder_insert(subRoot)
    print(bt.isSubtree(bt.root,bt_subroot.root))