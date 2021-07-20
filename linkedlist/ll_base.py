class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        #self.prev=None

class LinkedList:
    head=None
    def insert(self,node):
        pass
    def delete(self,node):
        pass
    def exists(self,node):
        pass
    def printf(self,head):
        #self.head=head
        while head!=None:
            print(head.data)
            head = head.next
        else:
            print("Done")

if __name__=="__main__":
    A=Node("A")
    B=Node("B")
    C=Node("C")
    D=Node("D")
    E=Node("E")
    ll = LinkedList()
    ll.head = A
    A.next = B
    B.next = C
    C.next = D
    #D.next = E
    ll.printf(ll.head)
    D.next = E
    ll.printf(ll.head)