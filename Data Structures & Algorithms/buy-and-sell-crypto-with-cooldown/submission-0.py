class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        dp=[[0]*len(prices) for _ in range(2)]
        dp[0][0]=-prices[0]
        dp[1][0]=0
        dp[0][1]=max(dp[0][0],-prices[1])
        dp[1][1]=max(dp[1][0],dp[0][0]+prices[1])
        for i in range(2,len(prices)):
            dp[0][i]=max(dp[0][i-1],dp[1][i-2]-prices[i])
            dp[1][i]=max(dp[1][i-1],dp[0][i-1]+prices[i])
        return max(dp[0][-1],dp[1][-1])
