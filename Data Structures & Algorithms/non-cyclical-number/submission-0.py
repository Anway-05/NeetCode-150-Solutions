class Solution:
    def squared_sum(self,n):
        res=0
        while n>0:
            res+=(n%10)**2
            n//=10
        return res

    def isHappy(self, n: int) -> bool:
        visited=set()
        visited.add(n)
        num=n
        while self.squared_sum(num)!=1:
            num=self.squared_sum(num)
            if num in visited:
                return False
            visited.add(num)
        return True