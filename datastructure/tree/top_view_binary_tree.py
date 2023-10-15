"""
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6       7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the extreme ones only(i.e. leftmost and rightmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3

"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    
    def depth(self,root,direc,result):
        if root and root.val not in result:
            result.append(root.val)
        if not root:#(root.right or root.left):
            return
        if direc=="right" and root.right:
            self.depth(root.right,direc,result)
        if direc=="left" and root.left:
            self.depth(root.left,direc,result)    
        return result
    
    def depth(self,root,direc,result,dh):
        if root and (root.val,dh) not in result:
            result.append((root.val,dh))
        if not root:#(root.right or root.left):
            return
        if direc=="right" and root.right:
            self.depth(root.right,direc,result,dh=dh+1)
        if direc=="left" and root.left:
            self.depth(root.left,direc,result,dh=dh-1)
        return result

    def topView(self,root):
        if not root:
            return 
        result=[]
        result=self.depth(root,"left",result,dh=0)
        #print(result)
        result=result[::-1]
        self.depth(root,"right",result,dh=0)
        #print(result)
        return result
    
    def _topView(self,root):

        level=0
        level_node=[root]
        left=[]
        right=[]
        while level_node:
            for ix in range(len(level_node)):
                node=level_node.pop()
                if node.left and node.left.val:
                    left.insert(0,node.left.val)
                    level_node.append(node.left)
                if node.right and node.right.val:
                    right.append(node.right.val)
                    level_node.append(node.right)
                
        return left,right
if __name__=="__main__":
    root=[1,2,3,4,5,6,7] #[4, 2, 1, 3, 7]
    #root=[1,2,3] #213
    root=[2,1,10,None,None,3,None,None,6,4,9,None,5] #1 2 10 9
    bt=Solution()
    bt.root=bt.preorder_insert(root)
    #bt.preorder(bt.root,"root",bt.root)
    print(bt.topView(bt.root))