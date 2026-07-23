class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup={}
        for x in nums:
            if x not in lookup:
                lookup[x]=1
            else:
                lookup[x]+=1
        stored=[[] for _ in range(len(nums)+1)]
        for key,value in lookup.items():
            stored[value].append(key)
        ans=[]
        for i in range(len(stored)-1,-1,-1):
            for num in stored[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans

