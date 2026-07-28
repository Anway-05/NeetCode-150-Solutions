class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final=[]
        current=""
        options={"(":0,")":0}
        def dfs():
            nonlocal current
            if len(current)==2*n:
                final.append(current)
                return
            if options["("]<n:
                current+="("
                options["("]+=1
                dfs()
                ch=current[-1]
                current=current[:-1]
                options[ch]-=1
            if options[")"]<options["("]:
                current+=")"
                options[")"]+=1
                dfs()
                ch=current[-1]
                current=current[:-1]
                options[ch]-=1
        dfs()
        return final
            
