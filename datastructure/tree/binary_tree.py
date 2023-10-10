class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def __str__(self):
        return str(self.val)

class BinaryTree:
    def __init__(self,root=None):
        self.root=root
    
    def preorder(self,root,direction,parent):
        if not root:
            return
        print(parent.val,"->",root.val," -> ",direction)
        self.preorder(root.left,"left",root)
        self.preorder(root.right,"right",root)

    def get_parent_index(self,i):
        return i//2

    def get_child_index(self,i):
        return (2*i+1,2*i+2)

    def preorder_insert(self,arr):
        for idx,ele in enumerate(arr):
            arr[idx]=Node(ele)
        for idx,node in enumerate(arr):
            idx_left_child,idx_right_child=self.get_child_index(idx)
            if idx_left_child<len(arr):
                node.left=arr[idx_left_child]
            if idx_right_child<len(arr):
                node.right=arr[idx_right_child]
        return arr[0]

if __name__=="__main__":
    #root=[3,9,20,None,None,15,7]
    #root=[10,8,13,7,9,11,14,15,16,17]
    #root=[1,None,2,None,3] #false
    root=[1,2,3,4,5,6,None,8] #true
    bt=BinaryTree()
    bt.root=bt.preorder_insert(root)
    bt.preorder(bt.root,"",bt.root)
    """
                10
        8               13
    7       9       11      14
    """