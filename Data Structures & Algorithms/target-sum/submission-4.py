class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target)>sum(nums):
            return 0
        dp=[[0]*(2*sum(nums)+1) for _ in range(len(nums)+1)]
        offset=sum(nums)
        dp[0][offset]=1
        for i,num in enumerate(nums):
            for j in range(len(dp[0])):
                if dp[i][j]>0:
                    dp[i+1][j+num]+=dp[i][j]
                    dp[i+1][j-num]+=dp[i][j]
        return dp[-1][offset+target]
