
class ListNode:
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev=prev

class DoublyLinkedList:
	head=None
	def __call__(self,curr=None):
		print("--"*10)
		curr=curr or self.head
		ll_str=[]
		while curr is not None:
			ll_str.append(curr.data)
			curr=curr.next
		output="->".join(map(str,ll_str))
		print(output)
	
	def push(self,node_data):
		new_node=ListNode(node_data)
		new_node.next=self.head
		if self.head is not None:
			self.head.prev=new_node
		self.head=new_node

	def delete_at_end(self):
		"""Delete linked list"""
		curr=self.head
		while curr.next is not None:
			prev=curr
			curr=curr.next
		prev.next=None
		curr=None

unordered=DoublyLinkedList()
for ele in range(6):
	unordered.push(ele)
unordered()
unordered.delete_at_end()
unordered.insert_in_front(10)
unordered()
