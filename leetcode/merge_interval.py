
arr=[[1,3],[2,7],[2,4],[2,8],[9,12]]
arr=[[1,3],[2,6],[8,10],[15,18]] #[[1,6],[8,10],[15,18]]
#arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
#arr=[[1,2],[3,4],[5,6],[7,9]]

def merge_interval_overlapping(arr):
    arr.sort(key=lambda x:x[0])
    print(arr)
    index=0
    for ix in range(1,len(arr)):
        if arr[index][1]>=arr[ix][0]:
            arr[index][1]=max(arr[index][1],arr[ix][1])
        else:
            index+=1
            arr[index]=arr[ix]
    print(arr[:index+1])

def merge_interval_overlapping(arr):
    arr.sort(key=lambda x:x[0])
    print(arr)
    merged=[]
    for ele in arr:
        if not merged or merged[-1][1]<ele[0]:
            merged.append(ele)
        else:
            merged[-1][1]=max(merged[-1][1],ele[1])
    print(merged)

merge_interval_overlapping(arr)
