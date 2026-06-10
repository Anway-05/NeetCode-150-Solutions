class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup={}
        for x in strs:
            freq=[0]*26
            for c in x:
                freq[ord(c)-97]+=1
            key=tuple(freq)
            if key not in lookup:
                lookup[key]=[]
            lookup[key].append(x)
        return list(lookup.values())