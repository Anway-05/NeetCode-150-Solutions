class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup={}
        longest=0
        i,j=0,0
        highest_freq=0
        while j<len(s):
            if s[j] not in lookup:
                lookup[s[j]]=1
                highest_freq=max(highest_freq,lookup[s[j]])
            else:
                lookup[s[j]]+=1
                highest_freq=max(highest_freq,lookup[s[j]])
            if highest_freq+k>=j-i+1:
                longest=max(longest,(j-i+1))
            else:
                lookup[s[i]]-=1
                i+=1
            j+=1
        return longest

