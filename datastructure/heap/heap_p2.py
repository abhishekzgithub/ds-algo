import sys

class Heap(object):
    "max heap"
    def __init__(self):
        self.heap=[]
        
    def _heapify(self,current_node_index=0):
        if self.is_leaf(current_node_index):
            return
        parent_index=current_node_index
        left_index=self.left(parent_index)
        right_index=self.right(parent_index)
        parent = self.heap[current_node_index]
        left=self.heap[self.left(current_node_index)]
        right=self.heap[self.right(current_node_index)]
        if parent< left:
            self.swap(parent_index,left_index)
            self._heapify(left_index)
        if parent< right:
            self.swap(parent_index,right_index)
            self._heapify(right_index)

    def left(self, data_index):
        return data_index*2

    def right(self,data_index):
        return data_index*2+1

    def is_leaf(self, data_index):
        if data_index>=(len(self.heap))//2 and data_index<=(len(self.heap)):
            return True
        return False

    def parent(self, data_index):
        return data_index//2

    def insert(self,data):
        if len(self.heap)==0:
            self.heap.append(data)
        else:
            self.heap.append(data)
            data_index=len(self.heap)-1
            while self.heap[self.parent(data_index)]<self.heap[data_index]:
                self.swap(self.parent(data_index),data_index)
                data_index=self.parent(data_index)

    def delete(self,data):
        pass

    def swap(self, data_index1,data_index2):
        self.heap[data_index1],self.heap[data_index2]=self.heap[data_index2],self.heap[data_index1]

    def display(self):
        print(self.heap)

    def heapify(self):
        for ele in range(len(self.heap)):#,-1,-1):
            self._heapify(ele)

heap=Heap()
# heap.insert(10)
# heap.insert(9)
# heap.insert(8)
# heap.insert(7)
# heap.insert(11)
heap.heap=[1,2,3,4,56,7]
heap.display()
heap.heapify()
heap.display()