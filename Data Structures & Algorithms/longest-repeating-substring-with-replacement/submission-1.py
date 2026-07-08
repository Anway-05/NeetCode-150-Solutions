class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup={}
        highest_freq=0
        longest=0
        i,j=0,0
        while j<len(s):
            lookup[s[j]]=lookup.get(s[j],0)+1
            highest_freq=max(highest_freq,lookup[s[j]])
            if highest_freq+k>=(j-i+1):
                longest=max(longest,(j-i+1))
            else:
                lookup[s[i]]-=1
                i+=1
            j+=1
        return longest