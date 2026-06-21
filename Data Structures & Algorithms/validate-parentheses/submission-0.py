class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            elif stack and ch == ']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif stack and ch == '}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif stack and ch == ')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True