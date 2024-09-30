class Stack(object):
    def __init__(self,size):
        self.stack=[-1]*5

    def push(self, element):
        if not self.is_full():
            for index,value in enumerate(self.stack):
                if value==-1:
                    self.stack[index]=element
                    break
        else:
            raise Exception(f"{element} cannot be inserted.")

    def pop(self):
        for index in range(1,len(self.stack)):
            if self.stack[len(self.stack)-index]!=-1:
                print("popping")
                self.stack[len(self.stack)-index] =-1
                break

    def is_full(self):
        if self.stack[len(self.stack)-1] != -1:
            return True
        return False
    def print_stack(self):
        print(self.stack)


# obj=Stack(5)
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(5)
# obj.print_stack()
# #obj.push(6)
# # obj.print_stack()
# print(obj.is_full())

