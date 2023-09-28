"""
https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/
Recursive Programs to find Minimum and Maximum elements of array

Input: arr = {1, 4, 3, -5, -4, 8, 6};
Output: min = -5, max = 8

Input: arr = {1, 4, 45, 6, 10, -8};
Output: min = -8, max = 45
"""
def func(arr, mini, maxi):
    if len(arr)-1>0:
        if mini>arr[0]:
            mini=arr[0]
        if maxi<arr[0]:
            maxi=arr[0]
        return func(arr[1:],mini,maxi)
    return mini,maxi

def func(arr, mini, maxi):
    if len(arr)-1<0:
        return mini,maxi
    if mini>arr[0]:
        mini=arr[0]
    if maxi<arr[0]:
        maxi=arr[0]
    return func(arr[1:],mini,maxi)

arr=[1, 4, 3, -5, -4, 8, 6]
print(func(arr,arr[0],arr[0]))