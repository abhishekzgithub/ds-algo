"""
https://leetcode.com/problems/maximum-width-of-binary-tree/description/
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-None nodes), where the None nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Input: root = [1,3,2,5,3,None,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,None,9).

Input: root = [1,3,2,5,None,None,9,6,None,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,None,None,None,None,None,7).

Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).

"""
from binary_tree import BinaryTree

class Solution(BinaryTree):

    def widthOfBinaryTree(self, root):
        def dfs(root,result,dp,vh,col,col_list):
            if not root:
                return
            if root and root.val:
                result.append((root.val,dp,vh,col))
                col_list.append(col)
            dfs(root.left,result,dp+1,vh-1,2*col,col_list)
            dfs(root.right,result,dp+1,vh+1,2*col+1,col_list)
        result=[]
        col_list=[]
        dfs(root,result,dp=0,vh=0,col=0,col_list=col_list)
        print (max(col_list)-min(col_list)+1)
        return result

#NOTE : todo
if __name__=="__main__":
    root = [1,3,2,5] #2
    root=[1,1,1,1,1,1,1,None,None,None,1,None,None,None,None,2,2,2,2,2,2,2,None,2,None,None,2,None,2] #8
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    print(bt.widthOfBinaryTree(bt.root))
