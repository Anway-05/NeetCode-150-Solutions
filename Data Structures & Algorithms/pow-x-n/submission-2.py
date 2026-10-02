class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative=n<0
        def power(x,n):
            if n==0:
                return 1
            half=power(x,n//2)
            if n%2==0:
                return half*half
            else:
                return half*half*x
        result=power(x,abs(n))
        if negative:
            return 1/result
        return result