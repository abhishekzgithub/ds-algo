class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def __str__(self):
        return str(self.val)

class BinaryTree:
    def __init__(self,root):
        self.root=root
    
    def insert(self,root,val):
        if root==None or val==None:
            return
        if val>root.val:
            if root.right:
                root.right=self.insert(root.right,val)
            else:
                root.right=Node(val)
        elif val<root.val:
            if root.left:
                root.left=self.insert(root.left,val)
            else:
                root.left=Node(val)
        return root
    
    def preorder(self,root,direction,parent):
        if not root:
            return
        print(parent.val,"->",root.val," -> ",direction)
        self.preorder(root.left,"left",root)
        self.preorder(root.right,"right",root)
    
    def get_height(self,root):
        height=[root]
        max_height=0
        while height:
            queue=[]
            for node in height:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height=queue
            max_height+=1
            print([h.val for h in height])
        print(max_height)
    
    def _get_height(self,root):
        height=[root]
        max_height=0
        while height:
            for ix in range(len(height)):
                node=height.pop(0)
                if node.left:
                    height.append(node.left)
                if node.right:
                    height.append(node.right)
            print("height",[h.val for h in height])
            max_height+=1
        print(max_height)
    
    def _depth_left(self,root,count=0):
        if not root:
            return count
        return self._depth_left(root.left,count+1)
        
    def _depth_right(self,root,count=0):
        if not root:
            return count
        return self._depth_right(root.right,count+1)

    def __depth(self,root): # doesnt pass all the results
        "worked for some cases"
        q=[root]
        height=0
        depth_right=0
        depth_left=0
        while q:
            height+=1
            for lvl in range(len(q)):
                print("At height",height)
                node=q.pop(0)
                print(f"processing NODE: {node}")
                if node.left:
                    depth_left=self._depth_left(node.left)
                    q.append(node.left)
                if node.right:
                    depth_right=self._depth_right(node.right)
                    q.append(node.right)
                print(depth_left,depth_right)
                if abs(depth_left-depth_right)>1:
                    return False
        return True

    def depth(self,root):
        "postorder traversal;LRP"
        if not root:
            return 0
        left = self.depth(root.left)
        right=self.depth(root.right)
        print(left,right)
        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        return 1+ max(left,right)

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

#root=[3,9,20,None,None,15,7]
#root=[10,8,13,7,9,11,14,15,16,17]
#root=[1,None,2,None,3] #false
root=[1,2,3,4,5,6,None,8] #true
bt=BinaryTree(Node(root[0]))
bt.root=bt.preorder_insert(root)
print("Depth",bt.depth(bt.root))
# for ele in root[1:]:
#     bt.insert(bt.root,ele)
bt.preorder(bt.root,"",bt.root)
"""
            10
    8               13
7       9       11      14
""" 
"""
            1
                2
                    3
                        4
                            5
                                6
                                    none
                                        8
        
"""
#print(bt.get_height(bt.root))
