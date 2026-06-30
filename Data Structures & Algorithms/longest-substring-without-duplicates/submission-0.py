class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup=set()
        longest=0
        i,j=0,0
        while j<len(s):
            if s[j] not in lookup:
                lookup.add(s[j])
            else:
                while s[j] in lookup:
                    lookup.discard(s[i])
                    i+=1
                lookup.add(s[j])
            j+=1
            longest=max(longest,(j-i))
        return longest


