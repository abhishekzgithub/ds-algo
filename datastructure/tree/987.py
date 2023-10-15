"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
"""
from collections import defaultdict
from binary_tree import BinaryTree

class Solution(BinaryTree):

    def dfs_original(self,root,at_level,vh,result):
        """This checks for the vertical height and level"""
        if not root:
            return None
        if root and root.val:
            result.append((root.val,at_level,vh))
            
        self.dfs_original(root.left,at_level+1,vh-1,result)
        self.dfs_original(root.right,at_level+1,vh+1,result)
        return result

    def dfs(self,root,at_level,vh,result,vh_queue):
        """This checks for the vertical height and level"""
        if not root:
            return None
        if root and root.val and vh not in vh_queue:
            result.append((root.val,at_level,vh))
            vh_queue.append(vh)
            
        self.dfs(root.left,at_level+1,vh-1,result,vh_queue)
        self.dfs(root.right,at_level+1,vh+1,result,vh_queue)
        return result

    def dfs(self,root,at_level,vh,result,vh_queue):
        """This checks for the vertical height and level"""
        if not root:
            return None
        if root and root.val:# and vh not in vh_queue:
            result.append((root.val,at_level,vh))
            vh_queue[vh].append(root.val)
            
        self.dfs(root.left,at_level+1,vh-1,result,vh_queue)
        self.dfs(root.right,at_level+1,vh+1,result,vh_queue)
        return result,vh_queue

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        at_level=0
        vh=0
        result=[]
        vh_queue=defaultdict(list)
        self.dfs(root,at_level,vh,result,vh_queue)
        result=sorted(result,key= lambda x:x[2])
        vh_queue=dict(sorted(vh_queue.items()))
        vh_queue=list(vh_queue.values())

        for idx in range(len(vh_queue)):
            vh_queue[idx]=sorted(vh_queue[idx])

        return result,list(vh_queue)

    
    def verticalTraversal(self, root):
        """
        Bottom view traversal
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root,at_level,vh,result,vh_queue):
            """This checks for the vertical height and level"""
            if not root:
                return None
            if root and root.val:# and vh not in vh_queue: for top view
                result.append((root.val,at_level,vh))
                if vh_queue.get(vh,None):
                    vh_queue[vh]=root.val # for bottom view
                else:
                    vh_queue[vh]=root.val
            dfs(root.left,at_level+1,vh-1,result,vh_queue)
            dfs(root.right,at_level+1,vh+1,result,vh_queue)
            return result,vh_queue

        at_level=0
        vh=0
        result=[]
        vh_queue={}
        dfs(root,at_level,vh,result,vh_queue)
        result=sorted(result,key= lambda x:x[2])
        vh_queue=dict(sorted(vh_queue.items()))
        vh_queue=list(vh_queue.values())
        return result,vh_queue

    
if __name__=="__main__":
    root = [1,2,3,4,5,6,7] #[4, 2, 6, 3, 7]
    root=[1,2,3,4,6,5,7]#[[4],[2],[1,5,6],[3],[7]]
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    #bt.preorder(bt.root,"root",bt.root)
    print(bt.verticalTraversal(bt.root))