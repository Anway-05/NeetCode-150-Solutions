class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        max_area=0
        def dfs(i,j):
            area=0
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1:
                return 0
            if (i,j) in visited:
                return 0
            if grid[i][j]==0:
                return 0
            if grid[i][j]==1:
                visited.add((i,j))
                area=1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)+dfs(i,j+1)
                return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    max_area=max(max_area,dfs(i,j))
        return max_area
            