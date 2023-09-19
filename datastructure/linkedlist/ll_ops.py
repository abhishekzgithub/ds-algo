
class ListNode:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class UnorderedList:
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
		self.head=new_node
	
	def delete_at_end(self):
		"""Delete linked list"""
		curr=self.head
		while curr.next is not None:
			prev=curr
			curr=curr.next
		prev.next=None
		curr=None
	
	def find_middle(self):
		curr=self.head
		curr_2=self.head
		while curr is not None and curr_2.next!=None and curr_2.next.next is not None:
			curr=curr.next
			curr_2=curr_2.next.next
		print(curr.data)

	def reverse(self, head):
		prev=ListNode()
		curr=head or self.head
		while curr is not None:
			next=curr.next
			curr.next=prev
			prev=curr
			curr=next
		#self.head=prev # assign the second last value to head
		return prev

	def loop(self):
		curr=self.head
		curr_2=self.head
		while curr_2.next!=None and curr_2.next.next is not None:
			curr=curr.next
			curr_2=curr_2.next.next
			if curr==curr_2:
				print(True)
				return curr
		print(False)
		return False

	def is_palindrome(self):
		curr=self.head
		dummy=self.head
		fast_curr=self.head
		while fast_curr.next!=None and fast_curr.next.next!=None:
			curr=curr.next
			fast_curr=fast_curr.next.next
		curr.next=self.reverse(curr.next)
		curr=curr.next
		while curr.next!=None:
			print(curr.data,dummy.data)
			if dummy.data!=curr.data:
				return False
			curr=curr.next
			dummy=dummy.next
		return True
	
	def remove_nth_node(self,node_val):
		curr=self.head
		prev=ListNode()
		count=0
		while curr.next!=None and count<node_val:
			prev=curr
			curr=curr.next
			count+=1
		if count==node_val:
			next=curr.next
			prev.next=next
		elif count<node_val:
			print("index not found")
			return
				


unordered=UnorderedList()
for ele in range(10):
	unordered.push(ele)

for ele in range(10,-1,-1):
	unordered.push(ele)
unordered()
#unordered.delete_at_end()
#unordered.push(9)

#unordered.find_middle()
#unordered.reverse()
#unordered()
#print(unordered.is_palindrome())
print(unordered.remove_nth_node(4))
unordered()