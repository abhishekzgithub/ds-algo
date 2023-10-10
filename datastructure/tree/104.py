"""
https://www.educative.io/answers/binary-trees-in-python
"""
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    
    def insert(self,val):
        if not val:
            return
        if self.val>val:
            if self.right:
                self.right.insert(val)
            else:
                self.right=Node(val)
                return self
        elif self.val<val:
            if self.left:
                self.left.insert(val)
            else:
                self.left=Node(val)
                return self

    def inorder(self,direction=""):
        if self.left:
            self.left.inorder("left")
        print(self.val,direction)
        if self.right:
            self.right.inorder("right")

    def depth(self,root,count=0):
        if not root:
            return count
        return max(self.depth(root.left,count+1),self.depth(root.right,count+1))
    
def test_case():
    root=Node(100)
    root.insert(90)
    root.insert(14)
    root.insert(74)
    root.insert(24)
    root.inorder()
    print(root.depth(root))

if __name__=="__main__":
    node_array=[3,9,20,None,None,15,7]
    root=Node(node_array[0])
    for ele in node_array[1:]:
        root.insert(ele)
    root.inorder()
    print(root.depth(root))



    