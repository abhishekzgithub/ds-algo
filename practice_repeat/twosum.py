class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remaining={}
        for index,ele in enumerate(nums):
            diff=target-ele
            if diff not in remaining:
                remaining[ele]=index
            else:
                return index, remaining[diff]

nums = [2,7,11,15]
target = 9
Output=[0,1]
print(Solution().twoSum(nums,target))
