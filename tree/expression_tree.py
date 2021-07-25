"""
prefix expression -> root will be first and then as usual left and right
root left right
loop over the expression
if we get operand i.e. numbers, return
else if we get the operator i.e. +,- etc, then create a node and pop two operands and assign it to the left and right  

expression tree:

for prefix, e.g.="+51"
algo:
read from back
if number:
push numbers in the stack
if operator:
    pop two operands
    and then push the current operator with the popped two operands i.e in a manner; '1' '+' '5'

for postfix, eg="51+"
algo:
read from front
    and same algo as prefix

for infix, eg="1+5":
    no need, as it can be directly evaluated
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left=None
    def __str__(self):
        return str(self.data)

class ExpressionTree:
    def __init__(self, root):
        self.root=root
        self.stack=[]
        self.evaluate=[]

    def prefix_insert(self, node):
        if node not in OPERATORS:
            self.stack.append(Node(node))
        else:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            new_node = Node(node)
            new_node.right = op1
            new_node.left = op2
            self.stack.append(new_node)

    def postfix_insert(self, node):
        if node not in OPERATORS:
            self.stack.append(Node(node))
        else:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            new_node = Node(node)
            new_node.right = op1
            new_node.left = op2
            self.stack.append(new_node)

    def inorder(self, root):
        if root is None:
            return root
        if root.data in OPERATORS:
            print("(", end="")
            self.evaluate.append("(")
        self.inorder(root.left)
        print(root.data)
        self.evaluate.append(root.data)
        self.inorder(root.right)
        if root.data in OPERATORS:
            print(")", end="")
            self.evaluate.append(")")
    def preorder(self, root):
        if root is None:
            return root
        self.preorder(root.left)
        print(root.data)
        self.preorder(root.right)
    
    def evaluate_prefix_stack(self, formula):
        exps = list(formula)
        while len(exps) > 1:
            for i in range(len(exps)-2):
                if exps[i] in OPERATORS:
                    if not exps[i+1] in OPERATORS and not exps[i+2] in OPERATORS:
                        op, a, b = exps[i:i+3]
                        a,b = map(float, [a,b])
                        c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[op]
                        exps = exps[:i] + [c] + exps[i+3:]
                        break
            print(exps)
        return exps[-1]

prefix ="+51"
#prefix = "*+34/76"
postfix = "ab+cde+**"
postfix="15+"
output=6

OPERATORS = ["+","-","*","/"]

print(prefix)
#in_data = ",".join(in_data)
#print(in_data)

# root =
et = ExpressionTree(Node(prefix[0]))
# root = et.root
# for ele in (in_data[1:]):
#     root = et.insert(root, (ele))

# et.preorder(root)
#et.evaluate_prefix_stack(in_data)#'1+(3+4*6+6*1)*2/3')

# for ele in reversed(prefix):
#     et.prefix_insert(ele)

for ele in (postfix):
    et.postfix_insert(ele)
#print(et.stack)
root = et.stack[-1]
print("root",root)
et.inorder(root)
print("\n")
print(et.evaluate)
#print("val", val)
#print(eval(et.evaluate))