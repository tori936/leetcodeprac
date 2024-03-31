from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_valid = {i:[] for i in range(9)}
        column_valid = {i:[] for i in range(9)}
        cells_valid= {x: {y: [] for y in range(3)} for x in range(3)}
        for row,col in enumerate(board):
            for i, value in enumerate(col):
                if value != ".":
                    if value in row_valid[row] or value in column_valid[i] or value in cells_valid[row//3][i//3]:
                        return False
                    row_valid[row]+=value
                    column_valid[i]+=value
                    cells_valid[row//3][i//3]+=(value)
        return True
Hmph = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Hmph.isValidSudoku(board))
board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Hmph.isValidSudoku(board2))
