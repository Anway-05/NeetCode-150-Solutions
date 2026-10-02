class Solution:
    def squared_sum(self,n):
        res=0
        while n>0:
            res+=(n%10)**2
            n//=10
        return res
        
    def isHappy(self, n: int) -> bool:
        slow,fast=n,n
        while slow!=1:
            slow=self.squared_sum(slow)
            fast=self.squared_sum(self.squared_sum(fast))
            if slow==fast:
                if slow==1:
                    return True
                return False
        return True