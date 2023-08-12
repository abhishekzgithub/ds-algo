"""
2119. A Number After a Double Reversal
Easy
567
31
Companies
Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

"""
import math

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        new_num=str(num)
        rev_num=""
        for ele in range(len(new_num)-1,-1,-1):
            rev_num+=new_num[ele]
        #rev_num=int(rev_num)
        new_rev_num=""
        for ele in range(len(str(rev_num))-1,-1,-1):
            new_rev_num+=rev_num[ele]
        return rev_num,new_rev_num
    
    def get_rev(self,num):
        rev_num=0
        length=int(math.log10(num))+1
        while length>0:
            rem=num%10
            num=int(num/10)
            rev_num+=rem*10**(length-1)
            length-=1
        return rev_num

    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        div=0
        rem=0
        rev_num=self.get_rev(num)
        new_rev_num=self.get_rev(rev_num)
        
        return num==new_rev_num


num=52600
print(Solution().isSameAfterReversals(num))