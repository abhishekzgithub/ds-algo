def func(arr):
    if len(arr)<=0:
        return 0
    return arr[0]+func(arr[1:])

print(func([1,8,9]))