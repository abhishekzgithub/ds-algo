"""
https://leetcode.com/problems/diameter-of-binary-tree/solutions/1515564/python-easy-to-understand-solution-w-explanation/
"""
from binary_tree import BinaryTree

class Solution(BinaryTree):
	def __init__(self):
		self.diameter = 0  # stores the maximum diameter calculated
	
	def depth(self, node):
		"""
		This function needs to do the following:
			1. Calculate the maximum depth of the left and right sides of the given node
			2. Determine the diameter at the given node and check if its the maximum
		"""
		# Calculate maximum depth
		left = self.depth(node.left) if node.left else 0
		right = self.depth(node.right) if node.right else 0
		# Calculate diameter
		if left + right > self.diameter:
			self.diameter = left + right
		# Make sure the parent node(s) get the correct depth from this node
		return 1 + max(left,right)
	
	def diameterOfBinaryTree(self, root):
		# if not root:
		#     return 0
		self.depth(root)  # root is guaranteed to be a TreeNode object
		return self.diameter

if __name__=="__main__":
	root = [1,2,3,4,5] #3
	bt=Solution()
	bt.root=bt.preorder_insert(root)
	print(bt.diameterOfBinaryTree(bt.root))
	#bt.preorder(bt.root,"parent",bt.root)
	#bt.postorder(bt.root)