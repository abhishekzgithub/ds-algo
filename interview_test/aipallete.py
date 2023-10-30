"""
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

"""

def check_palindrome(val):
    if len(val)==1:
        return False
    return val[::-1]==val

def dfs():
    pass

def longestPalindrome(s):
    max_pal=0
    result=[]
    i=0
    j=1
    if len(s)==1:
        return s
    
    while i<len(s) and j<len(s)-1:
        if s[i]==s[j]:
            print(s[i:j+1])
            if check_palindrome(s[i:j+1]):
                result.append(s[i:j+1])
                max_pal=max(max_pal,j-i)
            i+=1
        else:
            j+=1
    return max_pal+1,result


s="babad"
s = "cbbd"
#print(check_palindrome("sbobs"))
print(longestPalindrome(s))