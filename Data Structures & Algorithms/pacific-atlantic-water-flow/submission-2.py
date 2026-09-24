from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=[[False]*len(heights[0]) for _ in range(len(heights))]
        atlantic=[[False]*len(heights[0]) for _ in range(len(heights))]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        dq=deque()

        for j in range(len(heights[0])):
            pacific[0][j]=True
            dq.append((0,j))

        for i in range(1,len(heights)):
            pacific[i][0]=True
            dq.append((i,0))

        while dq:
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=len(heights) or nj>=len(heights[0]):
                    continue
                if not pacific[ni][nj] and heights[i][j]<=heights[ni][nj]:
                    pacific[ni][nj]=True
                    dq.append((ni,nj))

        for j in range(len(heights[0])):
            atlantic[len(heights)-1][j]=True
            dq.append((len(heights)-1,j))

        for i in range(0,len(heights)-1):
            atlantic[i][len(heights[0])-1]=True
            dq.append((i,len(heights[0])-1))

        while dq:
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=len(heights) or nj>=len(heights[0]):
                    continue
                if not atlantic[ni][nj] and heights[i][j]<=heights[ni][nj]:
                    atlantic[ni][nj]=True
                    dq.append((ni,nj))

        results=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    results.append([i,j])

        return results
        



                


