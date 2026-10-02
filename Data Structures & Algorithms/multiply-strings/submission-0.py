class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_=0
        for ch in num1:
            num1_=num1_*10+ord(ch)-ord('0')
        num2_=0
        for ch in num2:
            num2_=num2_*10+ord(ch)-ord('0')
        return str(num1_*num2_)
        