class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        current=[]
        candidates.sort()
        def dfs(i,result):
            if result==target:
                final.append(current.copy())
                return 
            if i==len(candidates):
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if result + candidates[j] > target:
                    break
                current.append(candidates[j])
                dfs(j+1,result+candidates[j])
                current.pop()
        dfs(0,0)
        return final

                