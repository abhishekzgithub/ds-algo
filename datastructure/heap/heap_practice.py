
class Node:
    def __init__(self, data=None):
        self.data=data
        self.right=None
        self.left=None

class MaxHeap:

    def __init__(self):
        self.heap=[]
        self.root=None

    def insert(self, ele):
        """
        adding the element at the end of the array to preserve the complete binary tree structure
        """
        if len(self.heap) == 0:
            self.heap.append(ele)
        else:
            self.heap.append(ele)
            for index in range((len(self.heap)//2)-1,-1,-1):
                self.heapify((self.heap),len(self.heap),(index))
    
    def check_complete_binary_tree(self):
        pass

    def delete_node(self, num):
        ele = self.heap.pop(0)
        return ele


    def heapify(self,heap_array, n, i):
        print(self.heap)
        largest=i
        left_index = 2 * i + 1 #self.get_left_node(heap_array[largest])
        right_index = 2 * i + 2  #self.get_right_node(heap_array[largest])

        if left_index<n and heap_array[i]<heap_array[left_index]:
            largest=left_index

        if right_index<n and heap_array[largest]< heap_array[right_index]:
            largest=right_index

        if largest!=i:
            heap_array[i], heap_array[largest]=heap_array[largest], heap_array[i]
            self.heapify(heap_array,n,largest)


    def get_parent(self, ele):
        parent = self.heap.index(ele)//2
        return self.heap[parent]
    
    def get_index_heap(self, ele):
        return self.heap.index(ele)

    def get_left_node(self, ele):
        left_index = (self.heap.index(ele)*2)+1
        return left_index

    def get_right_node(self, ele):
        right_index = (self.heap.index(ele)*2)+2
        return right_index

    def __str__(self):
        return str([i for i in self.heap])

heap=MaxHeap()
heap.insert(3)
heap.insert(4)
heap.insert(9)
heap.insert(5)
heap.insert(2)
heap.insert(10)
# heap.insert(11)

# print(heap.get_parent((4)))
# print(heap.get_left_node((4)))
# print(heap.get_right_node((4)))
print(heap)
#[3, 4, 9, 2, 5]
#o/p- [9, 5, 4, 3, 2]