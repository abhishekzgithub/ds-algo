def fibonacci(num):
    if num==0 or num==1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

num=7
for ele in range(num):
    (fibonacci(ele))

def prime_number(num):
    for ix in range(2,int(num/2)+1):
        if num%ix==0:
            print(ix)
            return False    
    return True

def prime_number(num):
    for ix in range(2,num):
        if num%ix==0:
            return False
    return True

def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

print(gcd(2,3))
print(prime_number(231))
print(prime_number(2))
print(prime_number(3))

for ele in range(1,100):
    print(prime_number(ele))