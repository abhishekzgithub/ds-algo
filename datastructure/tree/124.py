"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
    def maxPathSum(self, root):
        if not root:
            return root

        def dfs(root):
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            if root.val==None:
                root.val=0
            self.max_result=max(self.max_result, root.val+left+right)
            return max(root.val+max(left,right),0)
        self.max_result=root.val
        dfs(root)
        return self.max_result

if __name__=="__main__":
    root = [4,2,7,1,3,6,9] #[4,7,2,9,6,3,1]
    root=[1,2,3]
    #root = [-10,9,20,None,None,15,7]# 42
    #root =[1,-2,3] #4
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    print(bt.maxPathSum(bt.root))