"""
https://www.geeksforgeeks.org/reverse-a-linked-list/
take three pointers: prev, curr, next
"next" is the reference to next element.
step1: take the "next" reference of current and point it to prev.
step2: swap the prev to current and then current to next
step3: once curr rreaches to last, swap the head variable to "prev"

"""

class ListNode:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class UnorderedList:
	head=None

	def printll(self,curr=None):
		print("--"*10)
		curr=curr or self.head
		while curr is not None:
			print(curr.data)
			curr=curr.next

	def reverse(self):
		curr=self.head
		prev=ListNode()
		while curr is not None:
			next=curr.next
			curr.next=prev
			prev=curr
			curr = next
		self.head=prev
		self.printll(curr)


A=ListNode(1)
B=ListNode(2)
C=ListNode(3)
D=ListNode(4)

A.next=B
B.next=C
C.next=D
D.next=None
unordered=UnorderedList()
unordered.head=A
unordered.printll()
unordered.reverse()