class Solution(object):
   
		
	def find_parent(self,x,parent):
		if x==parent[x]:
			return parent[x]
		return self.find_parent(parent[x],parent)
	
	def do_union(self,x,y,rank,parent):
		parent_x=self.find_parent(x,parent)
		parent_y=self.find_parent(y,parent)
		if parent_x==parent_y:
			return
		if rank[parent_x]>rank[parent_y]:
			parent[parent_y]=parent_x
		elif rank[parent_y]>rank[parent_x]:
			parent[parent_x]=parent_y
		else:
			parent[parent_y]=parent_x
			rank[parent_x]+=1
	
	def findRedundantConnection(self, edges):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		rank=[]
		parent={}
		loop=False
		prerequisites=edges
		numCourses=len(edges)+1

		for ix in range(numCourses):
			parent[ix]=ix
			rank.append(0)

		for x,y in prerequisites:
			if self.find_parent(x,parent)==self.find_parent(y,parent):
				loop=True
				print(x,y)
				return (x,y)
			else:
				self.do_union(x,y,rank,parent)
			print(rank[x],rank[y])
		return not loop