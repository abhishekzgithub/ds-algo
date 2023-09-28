"""
https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
Input : malayalam
Output : Yes
Reverse of malayalam is also
malayalam.

Input : max
Output : No
Reverse of max is not max.
"""

def func(string,*args):
    print(string)
    index,last_index=0,len(string)
    if index==last_index:
        return True
    if string[index]!=string[last_index-1]:
        return False
    return func(string[index+1:last_index-1])

in_str="malayalam"
#in_str="abc"
s=0
l=len(in_str)-1
print(func(in_str,s,l))