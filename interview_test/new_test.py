# def f(): 
#    print(s)
#    s = "hello"
#    print(s)

# s = "world"
# f()

def f():
    city = "TEST"
    def g():
        nonlocal city
        city = "WORLD"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)

city = "NOTHING"
f()
print("'city' in main: " + city)

"""
Before calling g: TEST
Calling g now:
After calling g: WORLD
'city' in main: NOTHING
"""

#Input: 
nums = [2,7,11,15]; target = 9
Output: [0,1]

#Example 2:
Input: nums = [3,2,4]; target = 6
Output: [1,2]

def func(nums,target):
    result_dict={}
    for idx in range(len(nums)):
        next_element=target-nums[idx]
        if next_element in result_dict:
            return result_dict[next_element],idx
        else:
            result_dict[nums[idx]]=idx
    return result_dict
#O(n)
#O(k)
nums = [3,2,4]; target = 6
nums = [2,7,11,15]; target = 9
print(func(nums,target))

print(True, True, True == (True, True, True))