"""
https://www.geeksforgeeks.org/coin-change-dp-7/
Given an integer array of coins[ ] of size N representing different types of denominations and an integer sum, the task is to find the number of ways to make sum by using different denominations.  

Note: Assume that you have an infinite supply of each type of coin. 

Examples: 

Input: sum = 4, coins[] = {1,2,3}, 
Output: 4
Explanation: there are four solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}. 

Input: sum = 10, coins[] = {2, 5, 3, 6}
Output: 5
Explanation: There are five solutions: 
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
"""

def permute(string_val, state, hash,summ=10,index=0):
    """
    this solution uses the tabular or bottom-up approach where the solution is presented as the end
    the stopping condition specifies where to stop at the bottom
    """
    if sum(state)==summ:
        hash.append(state[::])
        return
    if sum(state)>summ:
        return False
    for idx in range(index,len(string_val)):
        state.append(string_val[idx])
        permute(string_val, state, hash,summ,idx)
        state.pop()
    return hash

target=10
print(permute([2,5,3,6],[],[],summ=target))

#unfinished