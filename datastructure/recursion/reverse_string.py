
def func(string,n,placeholder):
    if n>=0:
        placeholder+=string[n]
        print(string[n],end=" ")
        return func(string,n-1,placeholder)
        #print(string, end=" ")
    return placeholder

def _func(string,n):
    rev=""
    while n>=0:
        rev+=string[n]
        n-=1
    print(rev)

string="abcdef"
n=len(string)-1
print(func(string,n,""))