'''linked list
implement stack using linked list
'''
class Node:
    def __init__(self,node) -> None:
        self.data=node
        self.next=None
class Stack:
    def __init__(self) -> None:
        self.head=None
    
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=Node(data)
            curr.next.next=None

    def pop(self):
        if self.head!=None:
            data=self.head.data
            self.head=self.head.next
            print(f"{data} is deleted")

    def display(self):
        print("-"*10)
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next

class Queue(Stack):
    def __init__(self) -> None:
        self.head=None

    def pop(self):
        curr=self.head
        while curr.next.next!=None:
            curr=curr.next
        data=curr.next.data
        curr.next=None
        print(f"{data} has been popped")


stack=Queue()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.pop()
stack.pop()
stack.display()