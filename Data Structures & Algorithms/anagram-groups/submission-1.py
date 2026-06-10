class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stored=[]
        lookup={}
        key=0
        for x in strs:
            sorted_x="".join(sorted(x))
            if sorted_x not in lookup:
                lookup[sorted_x]=key
                stored.append([])
                key+=1
            stored[lookup[sorted_x]].append(x)
        return stored
                    