"""
https://www.geeksforgeeks.org/sum-of-natural-numbers-using-recursion/
Input : 3
Output : 6
Explanation : 1 + 2 + 3 = 6

Input : 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15
"""

def func(num):
    if num<=1:
        return num
    return num+func(num-1)
    

num=3
#num=5
print(func(num))