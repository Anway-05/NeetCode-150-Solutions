class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final=[]
        current=[]
        def dfs(i):
            final.append(current.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                current.append(nums[j])
                dfs(j+1)
                current.pop()
        dfs(0)
        return final