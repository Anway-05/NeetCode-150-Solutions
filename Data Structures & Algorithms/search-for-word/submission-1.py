class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag=False
        rows,cols=len(board),len(board[0])
        visited=set()
        def dfs(i,j,index):
            nonlocal flag
            if flag:
                return
            if i>rows-1 or j>cols-1 or i<0 or j<0:
                return
            if (i,j) in visited:
                return
            if board[i][j] != word[index]:
                return 
            if index==len(word)-1:
                flag=True
                return
            index+=1
            visited.add((i,j))
            dfs(i-1,j,index)
            dfs(i,j-1,index)
            dfs(i+1,j,index)
            dfs(i,j+1,index)
            visited.remove((i,j))
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,0)
        return flag
            
