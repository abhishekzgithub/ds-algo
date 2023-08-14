"""
https://www.youtube.com/watch?v=lr72sVlXFAw&t=945s&ab_channel=MartySteppCS106CS193StanfordArchive
state space tree is backtracking where we take out a space and a state from the input
The state will keep on updating.
Think of it in a dfs where we go all the way to the bottom and not in a bfs manner.
Also, this is a backtracking not a recursion only, you need four things
1. stopping condition
2. set the state
3. recurse in a dfs manner
4. unset the state
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1:
            return [nums]
        hashlist=set()
        hashlist2=self.permute_helper(nums, [], hashlist)
        return hashlist2

    def permute_helper(self,string_val, state, hashlist):
        if not string_val:
            state=tuple(state)
            hashlist.add(state)
        for index in range(len(string_val)):
            # setting the 'state' here
            c = string_val.pop(index)
            state.append(c)
            self.permute_helper(string_val, state, hashlist)
            string_val.insert(index,c)
            state.remove(c)
        return hashlist

val='123'


def permute(string_val, state, hash):
    """
    this solution uses the tabular or bottom-up approach where the solution is presented as the end
    the stopping condition specifies where to stop at the bottom
    """
    if not string_val:
        #print(state)
        hash.add("".join(state))
        return # stopping condition
    for index in range(len(string_val)):
        # setting the 'state' here
        c = string_val.pop(index)
        state.append(c)
        permute(string_val, state, hash) #increasing the 'state' and modifying the 'string_val' space
        ##unset the state so that the next time when the function returns and move back
        # it should find unmodified version as the for loop continues
        string_val.insert(index,c) # by inserting here, we are backtracking it
        state.remove(c)
        #return ## donot return here
    return hash

hash=set()
val='2211' #[[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
def permute_helper(val):
    val = list(val)
    #val=[2,2,1,1]
    hash1=permute(val, [], hash)
    print(hash1)
    
    
permute_helper(val)