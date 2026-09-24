from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=[[False]*len(heights[0]) for _ in range(len(heights))]
        atlantic=[[False]*len(heights[0]) for _ in range(len(heights))]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        dq=deque()
        visited=set()

        for j in range(len(heights[0])):
            pacific[0][j]=True
            dq.append((0,j))
            visited.add((0,j))

        for i in range(1,len(heights)):
            pacific[i][0]=True
            dq.append((i,0))
            visited.add((i,0))

        while dq:
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=len(heights) or nj>=len(heights[0]):
                    continue
                if heights[i][j]<=heights[ni][nj]:
                    pacific[ni][nj]=True
                    if (ni,nj) not in visited:
                        dq.append((ni,nj))
                        visited.add((ni,nj))
        visited.clear()

        for j in range(len(heights[0])):
            atlantic[len(heights)-1][j]=True
            dq.append((len(heights)-1,j))
            visited.add((len(heights)-1,j))

        for i in range(0,len(heights)-1):
            atlantic[i][len(heights[0])-1]=True
            dq.append((i,len(heights[0])-1))
            visited.add((i,len(heights[0])-1))

        while dq:
            i,j=dq.popleft()
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if ni<0 or nj<0 or ni>=len(heights) or nj>=len(heights[0]):
                    continue
                if heights[i][j]<=heights[ni][nj]:
                    atlantic[ni][nj]=True
                    if (ni,nj) not in visited:
                        dq.append((ni,nj))
                        visited.add((ni,nj))

        results=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    results.append([i,j])

        return results
        



                


