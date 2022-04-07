# Definition for singly-linked list.
class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution(object):
    def __init__(self) -> None:
        self.head=None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        curr=head
        prev=None
        while curr:
            temp1=curr.next
            curr.next=prev
            prev=curr
            curr=temp1
        return prev

    def printf(self, head=None):
        print("-"*40)
        
        while head.next!=None:
            print(head.data)
            head = head.next
        print(head.data)

head = [1,2,3,4,5]
        
A=Node("A")
B=Node("B")
C=Node("C")
D=Node("D")
E=Node("E")
F=Node("F")
G=Node("G")
ll = Solution()
ll.head = A
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G

ll.reverseList(ll.head)