def func(nums):
    if nums==0:
        return 0
    return nums%10+func(nums//10)
print(func(123))