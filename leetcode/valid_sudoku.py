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
        """
        hash_dict={}
        delimiter="."
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] !=delimiter:
                    if (row,board[row][col]) not in hash_dict:
                        hash_dict[(row,board[row][col])]=col
                    else:
                        return False
        hash_dict={}
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] !=delimiter:
                    if (col,board[row][col]) not in hash_dict:
                        hash_dict[(col,board[row][col])]=row
                    else:
                        return False

        def validBoard(start_row, end_row, start_col, end_col):
            hash_dict={}
            for row in range(start_row,end_row):
                for col in range(start_col,end_col):
                    if board[row][col] !=delimiter:
                        if board[row][col] not in hash_dict:
                            hash_dict[board[row][col]]=(row,col)
                        else:
                            return False
            return True
        for row in range(0,len(board),3):
            for col in range(0,len(board[0]),3):
                start_row=row
                end_row=row+3
                start_col=col
                end_col=col+3
                value= validBoard(start_row, end_row, start_col, end_col)          
                if not value:
                    return value
        return True
board=[ ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
expected_result=True


board=[ [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]
        ]
expected_result=False
obj=Solution()
actual_result = obj.isValidSudoku(board)
print(actual_result)
assert actual_result==expected_result
