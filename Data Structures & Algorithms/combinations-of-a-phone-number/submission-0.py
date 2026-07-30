class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        phone = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}
        final=[]
        current=[]
        def combination(index):
            if index==len(digits):
                final.append("".join(current))
                return
            for ch in phone[digits[index]]:
                current.append(ch)
                combination(index+1)
                current.pop()
        combination(0)
        return final

                

            