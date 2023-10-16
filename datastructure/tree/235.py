"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
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

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root,result):
            if not root:
                return 0
            if root and root.val!=None:
                result.append(root)
            dfs(root.left,result)
            dfs(root.right,result)
            return result
        if root is None:
            return 
        stack=[root]
        right_count=[]
        left_count=[]
        while stack:
            node=stack.pop()
            if node.left:
                if node.left.val==p or node.left.val==q:
                    left_count=dfs(node.left,left_count)
                stack.append(node.left)
            if node.right:
                if node.right.val==q or node.right.val==p:
                    right_count=dfs(node.right,right_count)
                stack.append(node.right)
        if len(left_count)>len(right_count):
            tree=left_count
            subtree=right_count
        else:
            tree=right_count
            subtree=left_count
        print(list(map(str,tree)),list(map(str,subtree)))
        print(self.isSubtree(tree[0],subtree[0]))
        if self.isSubtree(tree[0],subtree[0]):
            return len(subtree)-1
        else:
            return len(tree)+len(subtree)-2

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        the solution has to find the common parent of the given nodes
        """
        while True:
            if root.val > p and root.val > q:
                root = root.left
            elif root.val < p and root.val < q:
                root = root.right
            else:
                return root

    def lowestCommonAncestor(self, root, p, q):
        if root is None or root.val==p or root.val==q:
            return root
        left =self.lowestCommonAncestor(root.left,p,q)
        right =self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root
        
    def lowestCommonAncestor(self, root, p, q):
        if root:
            # If the value of p node and the q node is greater than the value of root node...
            if root.val > p and root.val > q:
                return self.lowestCommonAncestor(root.left, p, q)
            # If the value of p node and the q node is less than the value of root node...
            elif root.val < p and root.val < q:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
if __name__=="__main__":
    root = [6,2,8,0,4,7,9,None,None,3,5]; p = 2; q = 8 #6
    #p = 2; q = 4 #2
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    print(bt.lowestCommonAncestor(bt.root,p,q))