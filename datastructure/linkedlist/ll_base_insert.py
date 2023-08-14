class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        #self.prev=None

class LinkedList:
    head=None
    def insert_at_start(self,head, node):
        """
        you need a temp. put the head in temp as it will be used later otherwise overwriting of values will happen.
        put the new node point/in head. and put the temp/head(i.e. the first element) in the node.next
        """
        temp = head
        head = node
        node.next = temp
    def insert_at_end(self, head, node): # todo
        temp = head
        while temp!=None:
            temp = temp.next
            if temp.next is None:
                break
        temp.next=node
        return head

    def delete(self,node):
        pass
    def exists(self,node):
        pass
    def printf(self, head=None):
        print("-"*40)
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
    F=Node("F")
    G=Node("G")
    ll = LinkedList()
    ll.head = A
    A.next = B
    B.next = C
    C.next = D
    #D.next = E
    #ll.printf(ll.head)
    D.next = E
    #ll.printf(ll.head)
    ll.insert_at_start(ll.head,F)
    ll.head=ll.insert_at_end(ll.head,G)
    ll.printf(ll.head)