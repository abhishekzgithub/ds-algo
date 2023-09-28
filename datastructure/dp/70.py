"""
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution(object):

    def _climb_stairs(self,ways,state,result,index,n):
        if sum(state)==n:
            result.append(state[::])
            return True
        
        if sum(state)>n:
            return False

        if sum(state)<n:
            for ix in range(index,len(ways)):
                state.append(ways[ix])
                self._climb_stairs(ways,state,result,ix,n=n)
                print("state ",state)
                state.pop()
        return result

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways=[1,2]
        state=[]
        result=[]
        index=0
        self._climb_stairs(ways,state,result,index,n=n)
        return (result)

print(Solution().climbStairs(4))