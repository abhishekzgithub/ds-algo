"""Given a set with distinct elements, find all of its distinct subsets.

https://www.educative.io/courses/grokking-the-coding-interview/gx2OqlvEnWG
Input: [1, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

"""

def find_subset():
    data=[1,5,3]
    new_data=set()
    new_data.add([])
    