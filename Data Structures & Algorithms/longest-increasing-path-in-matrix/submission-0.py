class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j):

            if dp[i][j]!=0:
                return dp[i][j]

            best=1

            for di,dj in directions:
                ni=i+di
                nj=j+dj

                if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]):
                    if matrix[i][j]<matrix[ni][nj]:
                        best=max(best,1+dfs(ni,nj))

            dp[i][j]=best
            return dp[i][j]

        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans=max(ans,dfs(i,j))
        
        return ans


