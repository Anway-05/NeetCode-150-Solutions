class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        i=len(digits)-1
        while digits[i]>=10:
            if i==0:
                digits.insert(0,digits[i]//10)
                digits[1]%=10
            else:
                digits[i-1]+=digits[i]//10
                digits[i]%=10
            i-=1
        return digits