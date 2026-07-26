import math
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final=[]
        current=[]
        def dfs(i,result):
            nonlocal target
            if result==target:
                final.append(current.copy())
                return
            if i==len(nums) or result>target:
                return
            current.append(nums[i])
            result+=nums[i]
            dfs(i,result)
            val=current.pop()
            result-=val
            dfs(i+1,result)
        dfs(0,0)
        return final
            