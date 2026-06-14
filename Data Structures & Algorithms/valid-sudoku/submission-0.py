class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_row=set()
        set_col=set()
        boxes={}
        for i in range(9):
            for j in range(9):
                boxes[(i//3,j//3)]=set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] not in set_row:
                        set_row.add(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in set_col:
                        set_col.add(board[j][i])
                    else:
                        return False

                if board[i][j] != ".":
                    if board[i][j] not in boxes[(i//3,j//3)]:
                        boxes[(i//3,j//3)].add(board[i][j])
                    else:
                        return False
            set_row.clear()
            set_col.clear()
        return True