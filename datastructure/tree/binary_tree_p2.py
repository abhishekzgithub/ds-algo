"""
https://takeuforward.org/binary-tree/binary-tree-traversal-inorder-preorder-postorder/
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self,root):
        self.root=root
    
    def insert(self,node,root):
        if root is None:
            return node
        if node.val and node.val>root.val:
            if root.right!=None:
                root.right=self.insert(node,root.right)
            else:
                root.right=node
                return root
        elif node.val and node.val<root.val:
            if root.left!=None:
                root.left=self.insert(node,root.left)
            else:
                root.left=node
                return root
        return root

    def print_tree(self,root,direction=""):#inorder LNR
        if root==None:
            return root
        self.print_tree(root.left,direction="left")
        print(str(root.val),direction)
        self.print_tree(root.right,direction="right")
    
    def search(self,root,val):
        if root.val==val:
            print("Found")
            return root
        elif val>root.val:
            if root.right:
                return self.search(root.right,val) #make sure to return
        elif val<root.val:
            if root.left:
                return self.search(root.left,val) #make sure to return
        return "Not Found"
    
    def delete(self,root,k):
        if root is None:
            return root
 
        # Recursive calls for ancestors of
        # node to be deleted
        if root.val > k.val:
            root.left = self.delete(root.left, k)
            return root
        elif root.val < k.val:
            root.right = self.delete(root.right, k)
            return root
    
        # We reach here when root is the node
        # to be deleted.
    
        # If one of the children is empty
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
    
        # If both children exist
        else:
    
            succParent = root
    
            # Find successor
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
    
            # Delete successor.  Since successor
            # is always left child of its parent
            # we can safely make successor's right
            # right child as left of its parent.
            # If there is no succ, then assign
            # succ.right to succParent.right
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
    
            # Copy Successor Data to root
            root.val = succ.val
    
            # Delete Successor and return root
            del succ
            return root

    def depth_iterative(self,root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue[::] # resetting the level
        print(f"Max depth is {depth}\n")

def test_case1():
    #for None, we need the array based implementation of insert method
    node_array=[3,9,20,None,None,15,7] #3
    bt=BinaryTree(Node(node_array[0]))
    for ele in node_array[1:]:
        bt.root=bt.insert(Node(ele),bt.root)
    bt.print_tree(bt.root)
    bt.depth_iterative(bt.root)

def test_case2():
    node_array=[3,9,20,None,None,15,7] #3
    bt=BinaryTree(Node(node_array[0]))
    bt.root=bt.insert(Node(9),bt.root)
    bt.root=bt.insert(Node(20),bt.root)
    bt.root=bt.insert(Node(15),bt.root)
    bt.root=bt.insert(Node(7),bt.root)

    bt.print_tree(bt.root)
    bt.depth_iterative(bt.root)

def test_case3():
    A=Node(1000)
    bt=BinaryTree(A)
    root=bt.insert(Node(9),bt.root)
    root=bt.insert(Node(11),bt.root)
    root=bt.insert(Node(6),bt.root)

    root=bt.insert(Node(8),bt.root)
    bt.print_tree(root)
    print("searching: ",bt.search(bt.root,11))
    print("searching: ",bt.search(bt.root,1))
    root=bt.delete(root,Node(9))
    bt.print_tree(root)

test_case2()