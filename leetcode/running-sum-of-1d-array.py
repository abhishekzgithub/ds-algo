#https://leetcode.com/problems/running-sum-of-1d-array/
def runningSum(list_nums):
    result = []
    for index,item in enumerate(list_nums):
        result.append(sum(list_nums[:index+1]))
    return result

input_items = [1,2,3,4]
output = [1,3,6,10]
print(runningSum(input_items))
