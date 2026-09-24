from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=0
        dq=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
                if grid[i][j]==2:
                    dq.append((i,j))
        if count==0:
            return 0
        timer=-1
        level=0
        while dq:
            if level==0:
                level=len(dq)
                timer+=1
            print(level,timer)
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=len(grid) or nj>=len(grid[0]):
                    continue
                if grid[ni][nj]==1:
                    grid[ni][nj]=2
                    count-=1
                    dq.append((ni,nj))
            level-=1
        if count==0:
            return timer
        else:
            return -1
        
