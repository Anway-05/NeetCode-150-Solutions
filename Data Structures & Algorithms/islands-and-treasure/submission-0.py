from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    dq.append((i,j))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while dq:
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj

                if ni<0 or nj<0 or ni>len(grid)-1 or nj>len(grid[0])-1:
                    continue
                
                if grid[ni][nj]==2147483647:
                    grid[ni][nj]=grid[i][j]+1
                    dq.append((ni,nj))
            
