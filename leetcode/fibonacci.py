def fib(num):
    if num in [0,1]:
        return num
    return fib(num-1) + fib(num-2)


print(fib(4))#3