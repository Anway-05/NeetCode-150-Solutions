class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
        max_len=0
        ith=-1
        jth=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if j-i<2:
                    dp[i][j]= s[i]==s[j]
                else:
                    dp[i][j]= s[i]==s[j] and dp[i+1][j-1]
                if dp[i][j]==True:
                    if j-i+1>max_len:
                        max_len=j-i+1
                        ith=i
                        jth=j
        return s[ith:jth+1]
        
        

                