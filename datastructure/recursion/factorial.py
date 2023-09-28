def func(n):
    if n==0 or n==1:
        return n
    return n*func(n-1)

n=6
print(func(n))