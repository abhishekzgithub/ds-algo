"""
https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/
Given an array Arr[] of size N, print all the subsets of the array.

Subset: A subset of an array is a tuple that can be obtained from the array by removing some (possibly all) elements of it

Example:
Input: N = 3, Arr = [1, 2, 3]
Output: {}
{1}
{1, 2}
{1, 2, 3}
{1, 3}
{2}
{2, 3}
{3}
Explanation: These are all the subsets that can be formed from the given array, it can be proven that no other subset exists other than the given output.

Input: N = 2, Arr = [2, 4]
Output: {}
{2}
{2, 4}
{4}
Explanation: These are all the subsets that can be formed from the given array, it can be proven that no other subset exists other than the given output.
"""
def _func(arr,state,result):
    
    if len(arr)==1: #base case
        result.append(state[::])
        return

    for i in range(len(arr)):
        new_num_array=arr[:i]+arr[i+1:]
        state.append(arr[i])
        #print(state,new_num_array,result)
        _func(new_num_array,state,result)
        state.pop()

    return result # result

def func(arr):
    state=[]
    result=[]
    return _func(arr,state,result)

arr=[1,2,3] #[[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
print(func(arr))