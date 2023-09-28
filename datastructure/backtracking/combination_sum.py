"""
https://www.geeksforgeeks.org/combinational-sum/
https://leetcode.com/problems/combination-sum/description/
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        stack=[]
        state=[]
        space=candidates
        stack.append((state, space))
        res=[]
        while stack:
            state, space= stack.pop()
            if sum(state)==target:
                res.append(state)
            if sum(state)<target:
                for indx in range(len(space)):
                    new_state=state + [space[indx]]
                    new_space=space[indx:]
                    stack.append((new_state, new_space)) 
        return res

class Solution(object):


    def _combinationSum(self,state, arr, target,result,index):
        
        if sum(state)==target:
            result.append(state[::])
            return 
        if sum(state)>target:
            return 
        for ix in range(index,len(arr)):
            state.append(arr[ix])
            print(state)
            self._combinationSum(state,arr,target,result,ix)
            state.pop()
        return result

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        state=[]
        result=[]
        index=0
        return self._combinationSum(state, candidates, target,result,index)


candidates=[1,2,3]
target=4 #[[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
#candidates=[2,4,6,8] 
#target=8 #[[2, 2, 2, 2], [2, 2, 4], [2, 6], [4, 4], [8]]
print(Solution().combinationSum(candidates,target))