class Solution:
    def climbStairs(self, n: int) -> int:
        memory={}
        def dfs(i):
            if i<=2:
                return i
            
            if i in memory:
                return memory[i]

            memory[i]=dfs(i-1)+dfs(i-2)
            return memory[i]
        return dfs(n)
        