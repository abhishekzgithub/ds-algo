arr=[9,8,7,6,2,3,4,5]

def merge_sort(l_array):
    if len(l_array)<=1:
        return
    print(l_array)
    low,high=0,len(l_array)-1
    mid=(low+high)//2
    left=l_array[:mid+1]
    merge_sort(left)
    print("-"*8)
    right=l_array[mid+1:]
    merge_sort(right)
    i,j,k=0,0,0
    print("!"*5)
    print(left)
    print(right)
    print("!"*5)
    while i<len(left) and j<len(right):# if j has more elements than i; it needs to be moved to below
        if left[i]<right[j]:
            l_array[k]=left[i]
            i+=1
        else:
            l_array[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        l_array[k]=left[i]
        i,k=i+1,k+1
    while j<len(right):
        l_array[k]=right[j]
        j,k=j+1,k+1
    print(l_array)

merge_sort(arr)