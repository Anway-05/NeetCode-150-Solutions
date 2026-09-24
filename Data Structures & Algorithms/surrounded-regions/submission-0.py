from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        surrounded=set()
        dq=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    if i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1:
                        dq.append((i,j))
                    else:
                        surrounded.add((i,j))

        while dq:
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>len(board)-1 or nj>len(board[0])-1:
                    continue
                if board[ni][nj]=='O' and (ni,nj) in surrounded:
                    surrounded.remove((ni,nj))
                    dq.append((ni,nj))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) in surrounded:
                    board[i][j]='X'
        
