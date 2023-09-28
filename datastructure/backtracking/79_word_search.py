"""

https://leetcode.com/problems/word-search/description/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

class Solution(object):
    
    def _exist(self,state,board,word,col,row,index):
        # this is the stopping condition 
        # when we have got all the words
        if index==len(word): #note: important
            return True
        if col<0 or col>=len(board):
            return False
        if row<0 or row>=len(board[0]):
            return False
        if (col,row) in state: #state use here
            return False

        if board[col][row]!=word[index]:
            return False

        state.append((col,row))
        res= (self._exist(state,board,word,col+1,row,index+1) \
            or self._exist(state,board,word,col-1,row,index+1) \
            or self._exist(state,board,word,col,row+1,index+1) \
            or self._exist(state,board,word,col,row-1,index+1))
        print(state)
        state.pop()#((col,row))
        return res
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        state=[]#set()
        for col in range(len(board)):
            for row in range(len(board[0])):
                if self._exist(state,board,word,col,row,index=0):
                    return True
        return False

board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCCED"#[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)]
print(Solution().exist(board,word))