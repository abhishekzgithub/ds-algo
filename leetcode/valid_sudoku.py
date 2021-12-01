"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        i//3 or j//3 signofies which block it belongs
        basically a limit such 0th block if in 0,1,2
        since we have row with blocks in 0,3,6,9
        """
        row_set=set()
        col_set=set()
        block=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                row_hash_key=(i, board[i][j])
                col_hash_key=(j, board[i][j])
                block_hash_key=(i//3,j//3, board[i][j])
                if board[i][j]!=".":
                    if (
                        row_hash_key in row_set
                        or col_hash_key in col_set
                        or block in block_hash_key
                    ):
                        return False
                    else:
                        row_set.add(row_hash_key)
                        col_set.add(col_hash_key)
                        block.add(block_hash_key)
        return True


board = [["5","3",".",
  ".","7",".",
  ".",".","."]

,["6",".",".",
  "1","9","5",
  ".",".","."]

,[".","9","8",
  ".",".",".",
  ".","6","."]

,["8",".",".",
  ".","6",".",
  ".",".","3"]

,["4",".",".",
  "8",".","3",
  ".",".","1"]

,["7",".",".",
  ".","2",".",
  ".",".","6"]

,[".","6",".",
 ".",".",".",
 "2","8","."]

,[".",".",".",
  "4","1","9",
  ".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


obj=Solution()
result = obj.isValidSudoku(board)
assert result