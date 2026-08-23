class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2 != 0:
            return False
        half=total//2
        dp=[False]*(half+1)
        dp[0]=True
        for i in range(len(nums)):
            for j in range(half,nums[i]-1,-1):
                if dp[j-nums[i]]:
                    dp[j]=True
        return dp[-1]

