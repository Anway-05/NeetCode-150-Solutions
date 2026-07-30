class Solution:
    def isPalindrome(self,s):
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        final=[]
        current=[]
        def dfs(index):
            if index==len(s):
                final.append(current.copy())
                return
            for end in range(index,len(s)):
                substring=s[index:end+1]
                if self.isPalindrome(substring):
                    current.append(substring)
                    dfs(end+1)
                    current.pop()
        dfs(0)
        return final                
        