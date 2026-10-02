class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_=0
        for ch in num1:
            num1_=num1_*10+ord(ch)-ord('0')
        num2_=0
        for ch in num2:
            num2_=num2_*10+ord(ch)-ord('0')
        product=num1_*num2_
        if product==0:
            return "0"
        result=""
        while product>0:
            n=chr(product%10+ord("0"))
            print(n)
            product//=10
            result=n+result
        return result
        