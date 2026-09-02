class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        n_2=1
        n_1=2
        while n>2:
            n_1,n_2=n_1+n_2,n_1
            n-=1
        return n_1