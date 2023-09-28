"""
https://www.geeksforgeeks.org/program-to-print-first-n-fibonacci-numbers/
Input: n = 3
Output: 0 1 1

Input: n = 7
Output: 0 1 1 2 3 5 8
"""
# recursive approach
# def func(num):
#     if num<=0 or num==1:
#         return num
#     return func(num-1)+func(num-2)

# n=7
# for i in range(n):
#     print(func(i),end=" ")

def funciter(num):
    f1=0
    f2=1
    print(f1,end=" ")
    for ix in range(1,num):
        print(f2,end=" ")
        temp=f1+f2
        f1=f2
        f2=temp
        
funciter(7)

