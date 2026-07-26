import math
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final=[]
        current=[]
        nums.sort()
        def dfs(i,result):
            if result==target:
                final.append(current.copy())
                return
            if i==len(nums) or result>target:
                return
            current.append(nums[i])
            dfs(i,result+nums[i])
            current.pop()
            dfs(i+1,result)
        dfs(0,0)
        return final
            