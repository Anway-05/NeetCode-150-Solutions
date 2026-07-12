class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        min_len=[float("inf"),-1,-1]
        lookup1={}
        lookup2={}
        for ch in t:
            lookup1[ch]=lookup1.get(ch,0)+1
        need=len(lookup1)
        have=0
        i,j=0,0
        while j<len(s):
            lookup2[s[j]]=lookup2.get(s[j],0)+1
            if s[j] in lookup1 and lookup2[s[j]]==lookup1[s[j]]:
                have+=1
            while need==have:
                if (j-i+1)<min_len[0]:
                    min_len[0]=j-i+1
                    min_len[1]=i
                    min_len[2]=j
                lookup2[s[i]]-=1
                if s[i] in lookup1 and lookup2[s[i]]<lookup1[s[i]]:
                    have-=1
                i+=1
            j+=1
        
        return "" if min_len[0]==float("inf") else s[min_len[1]:min_len[2]+1]

            
