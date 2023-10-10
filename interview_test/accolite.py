"""
8:
*######
**#####
***####
****###
***####
**#####
*######


"""

def pattern(num):
    i=1
    j=num-1
    queue=[None]*(num)
    print(queue)
    result=""
    while i<=j:
        if i%2!=0:
            print(i)
            result+='*'*i
            result+='#' *j
        else:
            print(i)
            result+='#' *j
            result+='*'*i
        result+="\n"
        print(result)
        queue[i-1]=result
        queue[-i]=result
        i+=1
        j-=1
        result=""
    print(i,j)
    
    print(queue)


def pattern(num,i,j,result):
    #print(result)
    if num==0:
        return result
    if num%2==0:
        return pattern(num-1,i+1,j-1,result=result+str("*"*i)+str("#"*j)+"\n")
    else:
        return pattern(num-1,i+1,j-1,result=result+str("#"*i)+str("*"*j)+"\n")
    return result

    
num=8
print(pattern(num-1,i=1,j=num-1,result=""))