class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lookup={'+':lambda a,b:a+b,
        '-':lambda a,b:a-b,
        '*':lambda a,b:a*b,
        '/':lambda a,b:int(a/b)}
        stack=[]
        for x in tokens:
            if x in lookup:
                a=stack.pop()
                b=stack.pop()
                stack.append(lookup[x](b,a))
            else:
                stack.append(int(x))
        return stack.pop()
