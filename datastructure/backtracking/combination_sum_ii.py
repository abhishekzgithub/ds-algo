"""
https://www.geeksforgeeks.org/combinational-sum/
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
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


    def _combinationSum(self,state, arr, target,result):
        
        if sum(state)==target:
            result.append(state[::])
            return result

        if sum(state)>target:
            return 0
        else:
            for ix in range(len(arr)):
                if ix>0 and arr[ix]==arr[ix-1]:
                    continue
                new_array=arr[::]
                state.append(new_array[ix])
                new_array=new_array[:ix]+new_array[ix+1:]
                self._combinationSum(state,new_array,target,result)
                state.pop()
        return result or 0
    
    def _combinationSum(self,state, arr, target,result):
        """
        look at the key:
        all it required you to move one by one in the index and leave prev
        """
        if sum(state)==target:
            result.append(state[::])
            return result

        if sum(state)>target:
            return 0
        else:
            for ix in range(len(arr)):
                if ix>0 and arr[ix]==arr[ix-1]:
                    continue
                new_array=arr[::]
                state.append(new_array[ix])
                new_array=new_array[ix+1:] # its the key
                self._combinationSum(state,new_array,target,result)
                state.pop()
        return result or 0
        

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        state=[]
        result=[]
        candidates.sort()
        return self._combinationSum(state, candidates, target,result)

class _Solution:
    def combinationSum2(self, candidates, target):
        
        def backtrack(nums,targetLeft,path):
            
            if targetLeft==0:
                res.append(path)
                return
            
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if nums[i]>targetLeft:
                    break
                backtrack(nums[i+1:],targetLeft-nums[i],path+[nums[i]])
            
        res=[]
        backtrack(sorted(candidates),target,[])
        return res

candidates=[1,2,3]
target=4 #[[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
#candidates=[2,4,6,8] 
#target=8 #[[2, 2, 2, 2], [2, 2, 4], [2, 6], [4, 4], [8]]
candidates = [10,1,2,7,6,1,5]
target = 8 #[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

print(Solution().combinationSum2(candidates,target))
#print(Solution().combinationSum2(candidates,target))