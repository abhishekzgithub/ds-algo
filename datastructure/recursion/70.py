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

    def _climb_stairs(self,index,state,stair_constraints,n,result):
        if sum(state)==n:
            result.append(state[::])
            return True
        if sum(state)>n:
            return False
        if sum(state)<n:
            for idx in range(index,len(stair_constraints)):
                state.append(stair_constraints[idx])
                self._climb_stairs(idx,state,stair_constraints,n,result)
                state.pop()
                #    return True
        return False

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stair_constraints=[1,2]
        result=[]
        state=[]
        index=0
        #for idx in range(len(stair_constraints)):
        self._climb_stairs(index,state,stair_constraints,n,result)
        return result

    def climbStairs(self,n):
        if n==1 or n==2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
    def climbStairs(self,n):
        memo={}
        memo[1]=1
        memo[2]=2
        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]=climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)
n=3 #3
n=2 #2
n=44

print(Solution().climbStairs(n))