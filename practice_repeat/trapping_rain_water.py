"""
https://www.geeksforgeeks.org/trapping-rain-water/

Given n non-negative integers representing an elevation
map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

input_1=[2, 0, 2,0,2]
input_2 = [3, 0, 2, 0, 4]
input_3=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
import copy
bucket=0
def get_bucket(input_data):
    global bucket
    new_input_data = copy.deepcopy(input_data)
    for _ in range(max(new_input_data)):
        new_input_data=[i-1 for i in new_input_data]
        print(new_input_data)
    #new_input_data=[i-1 for i in new_input_data]
    #print(new_input_data)
    bucket = sum(new_input_data)
    return bucket
print(get_bucket(input_2))
#assert get_bucket(input_1)==2
#assert get_bucket(input_2)==7
#assert get_bucket(input_3)==6