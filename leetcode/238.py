class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        go zig zag on array left/right to nums for left and right

        """
        array_left=[1]*(len(nums))
        array_right=[1]*(len(nums))
        m=1
        for ix, ele in enumerate(nums):
            array_right[ix]=m
            m=array_right[ix]*nums[ix]
        n=1
        for ix in range(1,len(nums)+1):
            array_left[-ix]=n
            n=array_left[-ix]*nums[-ix]    
        for ix in range(len(nums)):
            nums[ix]=array_right[ix]*array_left[ix]
        return nums

nums=[1,2,3,4]
print(Solution().productExceptSelf(nums))