"""
This is the ListNode class definition


"""
class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next


class Solution:
	def printLinkedList(self, head):
		# add your logic here
		while head is not None:
			print(head.data)
			head=head.next