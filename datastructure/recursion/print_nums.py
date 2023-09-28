"""
https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/
"""

def func(n):
    print(n, end=" ")
    if n>0:
        func(n-1)
        print(n, end=" ")

func(5)