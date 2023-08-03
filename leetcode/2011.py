"""
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""

class Solution:
    def finalValueAfterOperations(self, operations):
        x=0
        for ele in operations:
            if ele in ["X++","++X"]:
                x+=1
            else:
                x-=1
        return x

operations=["--X","X++","X++"]
print(
Solution().finalValueAfterOperations(operations)
)