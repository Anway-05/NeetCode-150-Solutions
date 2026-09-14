class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={
            0:1
        }
        for num in nums:
            new_dp={}
            for key in dp:
                new_dp[key-num]=new_dp.get(key-num,0)+dp[key]
                new_dp[key+num]=new_dp.get(key+num,0)+dp[key]
            dp=new_dp
        return dp.get(target,0)