"""
"Write a Python program to find element in a list from current element to next index  

      

list is [""Mon"",""Tue"",""Wed"",""Thu"",""Fri"",""Sat"",""Sun""]



If current element is “Wed” and next index is 2, result is “Fri”

If current element is “Sat” and next index is 23 (cyclic), result is “Mon”"

Wed,8 ->sat 
"""

def func(arr,ele,index):
    """elements are indexed as 1"""
    new_index=0
    for ix, val in enumerate(arr):
        if val==ele:
            new_index=(ix+index)%(len(arr))
            return arr[new_index]
arr=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(func(arr,"Wed",2)) #4
print(func(arr,"Sat",23)) #0


"""

"Input is an array of integers. There is a sliding window of size W which 

is moving from the very left of the array to the very right. Each time the sliding window moves rightwards by one position. Find the maximum number from each window. 

  

Input array is [1, 3, -1, -3, 5, 3, 6, 7] and Sliding window (W) is 3. 

Output array is [3, 3, 5, 5, 6, 7] "
"""

def func(arr,slide_window_size):
    result=[]
    for idx in range(len(arr)-slide_window_size+1):
        result.append(max(arr[idx:idx+slide_window_size]))
    return result
arr=[1, 3, -1, -3, 5, 3, 6, 7]
slide_window_size=3
print(func(arr,slide_window_size))

"""
to join 4or5 small tables.
1.to process 10gb /hour, capacity planning;
2.how to ensure, it completes in 1 hour, if it is not  then 1 gb on hold and consideration to catch up.
3. if one instance is free, how to make sure it is getting used again.

--
nodes=10
ram=2gb
It should be sufficient for the smaller tables.
2. Approach optimisation, 
"""





















