class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final=[]
        current=[]
        options={"(":0,")":0}
        def dfs():
            if len(current)==2*n:
                final.append("".join(current))
                return
            if options["("]<n:
                current.append("(")
                options["("]+=1
                dfs()
                ch=current.pop()
                options[ch]-=1
            if options[")"]<options["("]:
                current.append(")")
                options[")"]+=1
                dfs()
                ch=current.pop()
                options[ch]-=1
        dfs()
        return final
            
