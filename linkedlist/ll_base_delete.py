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
        return head

    def insert_at_end(self, head, node): # todo
        temp = head
        while temp.next!=None:
            temp = temp.next
        temp.next=node
        return head

    def delete(self,head,node):
        temp = head
        while temp.next!=node:
            temp=temp.next
        #temp.next = temp.next.next
        temp_node = temp.next
        temp.next = None
        temp.next = temp_node.next
        return head

    def exists(self,node):
        pass
    def printf(self, head=None):
        print("-"*40)
        
        while head.next!=None:
            print(head.data)
            head = head.next
        print(head.data)
        


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
    D.next = E
    ll.head = ll.insert_at_start(ll.head,F)
    ll.head=ll.insert_at_end(ll.head,G)
    ll.head = ll.delete(ll.head,E)
    ll.printf(ll.head)