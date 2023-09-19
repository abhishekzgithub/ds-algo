class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        just find the minimum out of the sum or x
        """
        summ=0
        x=0
        for ele in nums:
            summ+=ele
            x=min(summ,x)
        return -x+1

    def _minStartValue(self,x,nums):
        """This method doesnt care about other stuff.
            It only cares about x and its increment values.
            Once it finds the incremented values,it just
            returns it.
        """
        summ=x
        for ele in nums:
            summ+=ele
            if summ<1:
                return self._minStartValue(x+1,nums)
        return x

    def minStartValue(self,nums):
        x=1
        return self._minStartValue(x,nums)

nums=[-3,2,-3,4,2] # 5
print(Solution().minStartValue(nums))