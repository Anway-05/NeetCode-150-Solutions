class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            if len(nums)==1:
                return nums[0]
            rob0,rob1=0,0
            for num in nums:
                curr=max(rob0+num,rob1)
                rob0,rob1=rob1,curr
            return rob1
        if len(nums)==1:
            return nums[0]
        return max(
        house_robber(nums[:-1]),
        house_robber(nums[1:])
        )
