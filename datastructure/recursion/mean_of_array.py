"""
https://www.geeksforgeeks.org/mean-of-array-using-recursion/
Input : 1 2 3 4 5
Output : 3
"""

def func(arr, summ,arr_len):
    if len(arr)>0:
        ele = arr.pop()
        summ+=ele
        return func(arr,summ,arr_len)
    print(summ//arr_len)

ele=[1,2,3,4,5]
ele=[1,2,3]

summ=0
array_len=len(ele)
func(ele,summ,array_len)
