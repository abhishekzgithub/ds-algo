"""Foray"""
"""
wrote a method
params: arr, key
write a code to search for key in array, if key found, "found" else "not found"
"""
# def find_key(arr, key):
#     for ele in arr:
#         if ele==key:
#             return "found"
#     return "not found"

def find_key(arr, key):
    if isinstance(key,int):
        low=0
        high=len(arr)-1
        while low<high:
            mid=(high+(low-1))//2
            if key==arr[mid]:
                return "found"
            if key<arr[mid]:
                high-=1
            elif key>=arr[mid]:
                low+=1
    return 'not found'
            
print(find_key([1,2,3,4],3))
print(find_key([1,2,3,4],5))