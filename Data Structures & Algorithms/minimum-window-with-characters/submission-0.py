class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        lookup1={}
        lookup2={}
        max_list=[float('inf'),0,0]
        for ch in t:
            lookup1[ch]=lookup1.get(ch,0)+1
        i,j=0,0
        while j<len(s):
            flag=True
            lookup2[s[j]]=lookup2.get(s[j],0)+1
            for ch in lookup1:
                if not (lookup1[ch]<= lookup2.get(ch,0)):
                    flag=False
            while flag==True:
                if (j-i+1)<max_list[0]:
                    max_list[0]=j-i+1
                    max_list[1]=i
                    max_list[2]=j
                lookup2[s[i]]-=1
                if lookup2[s[i]]==0:
                    del lookup2[s[i]]
                i+=1
                for ch in lookup1:
                    if not (lookup1[ch]<= lookup2.get(ch,0)):
                        flag=False
            while i<=j and s[i] not in lookup1:
                lookup2[s[i]]-=1
                if lookup2[s[i]]==0:
                    del lookup2[s[i]]
                i+=1
            j+=1
        if max_list[0]==float('inf'):
            return ""
        else:
            return s[max_list[1]:max_list[2]+1]