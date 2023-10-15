"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[root]
        level_node=[[root.val]]
        level=[]
        at_level=1
        while queue:
            level=[]
            for nodes in range(len(queue)):
                nodes=queue.pop(0)
                if nodes.left and nodes.left.val!=None:
                    level.append(nodes.left.val)
                    queue.append(nodes.left)
                if nodes.right and nodes.right.val!=None:
                    level.append(nodes.right.val)
                    queue.append(nodes.right)    
            print(level,at_level)
            if level:
                if at_level%2!=0:
                    level=level[::-1]
                level_node.append(level)
            at_level+=1
        
        print(level_node)



if __name__=="__main__":
    #root = [3,9,20,None,None,15,7,11,16]
    root = [3,9,20,15,7,11,16]
    root=[1,2,3,4,None,None,5] #[[1],[3,2],[4,5]]
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    bt.zigzagLevelOrder(bt.root)