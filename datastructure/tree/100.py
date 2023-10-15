"""
https://leetcode.com/problems/same-tree/description/
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true
Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

"""
from binary_tree import BinaryTree, Node

class Solution(BinaryTree):
    def __init__(self,root=None):
        self.root=root

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None or q==None:
            return True
        return ((p.val==q.val) 
                and self.isSameTree(p.left,q.left) 
                and self.isSameTree(p.right,q.right))

if __name__=="__main__":
    p = [1,2,1]; q = [1,1,2] #false
    p = [1,2,3]; q = [1,2,3] #true
    bt_p,bt_q,solution=Solution(),Solution(),Solution()
    bt_p.root=bt_p.preorder_insert(p)
    bt_q.root=bt_q.preorder_insert(q)
    print(solution.isSameTree(bt_p.root,bt_q.root))
