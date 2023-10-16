"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        queue=[root]
        level_nodes=[[root.val]]
        while queue:
            at_level=[]
            for idx in range(len(queue)):
                node = queue.pop(0)
                if node.left and node.left.val!=None:
                    queue.append(node.left)
                    at_level.append(node.left.val)
                if node.right and node.right.val!=None:
                    queue.append(node.right)
                    at_level.append(node.right.val)
            if at_level!=[]:
                level_nodes.append(at_level)
        return level_nodes

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        queue=[root]
        level_nodes=[[root.val]]
        while queue:
            at_level=[]
            for idx in range(len(queue)):
                node = queue.pop(0)
                if node.left and node.left.val!=None:
                    queue.append(node.left)
                    at_level.append(node.left.val)
                if node.right and node.right.val!=None:
                    queue.append(node.right)
                    at_level.append(node.right.val)
            if at_level!=[]:
                level_nodes.append(at_level)
        return level_nodes[::-1]

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        queue=[root]
        level_nodes=[[root.val]]
        while queue:
            at_level=[]
            for idx in range(len(queue)):
                node = queue.pop(0)
                if node.left and node.left.val!=None:
                    queue.append(node.left)
                    at_level.append(node.left.val)
                if node.right and node.right.val!=None:
                    queue.append(node.right)
                    at_level.append(node.right.val)
            if at_level!=[]:
                level_nodes.append(at_level)
        print(level_nodes)
        for idx in range(len(level_nodes)):
            level_nodes[idx]=sum(level_nodes[idx])/len(level_nodes[idx])
        return level_nodes

if __name__=="__main__":
    root=[3,9,20,None,None,15,7]
    root=[1,2,3,4,None,None,5] #[[1],[2,3],[4,5]]
    root=[3,9,20,None,None,15,7] #[3.00000,14.50000,11.00000] avg
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    print(bt.levelOrder(bt.root))