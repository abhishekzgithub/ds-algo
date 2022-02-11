"""
https://www.geeksforgeeks.org/unrolled-linked-list-set-1-introduction/

"""

class Node:
    def __init__(self,data=None):
        self.next=None
        self.data=data
        self.data_length=len(data)

"""
[]->[]->[]->[]->[]-None
a   c       e   g
    d       f   h
    h
"""

def find_element(head, position):
    counter=0
    while head:
        if head.data and head.data_length>0:
            for ele in range(head.data_length):
                if position == counter:
                    return head.data[ele]
                counter+=1
        head=head.next
    return None

def find_element_optimized(head, position):
    #position-=1
    curr_value=0
    while head:
        if head.data and head.data_length>0:
            if curr_value+head.data_length<position:
                curr_value=curr_value+head.data_length
            else:
                for ele in range(head.data_length):
                    if position == curr_value:
                        return head.data[ele]
                    else:
                        curr_value=curr_value+1
        head=head.next
    return None

head=A=Node(data=['a','b','c'])
B=Node(data=['d'])
C=Node(data=[])
D=Node(data=['e','f'])
E=Node(data=['g','h'])
A.next=B
B.next=C
C.next=D
D.next=E

print(find_element_optimized(head, 0))