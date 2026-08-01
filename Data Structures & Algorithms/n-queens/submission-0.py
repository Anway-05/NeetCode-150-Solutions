class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        final=[]
        curr=[]
        column=set()
        right_diag=set()
        left_diag=set()
        def board(row):
            if len(curr)==n:
                final.append(curr.copy())
                return
            for col in range(n):
                if col in column or row+col in right_diag or row-col in left_diag:
                    continue
                curr.append("."*col+"Q"+"."*(n-col-1))
                column.add(col)
                right_diag.add(row+col)
                left_diag.add(row-col)
                board(row+1)
                curr.pop()
                column.remove(col)
                right_diag.remove(row+col)
                left_diag.remove(row-col)
        board(0)
        return final            
            