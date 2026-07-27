class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        current=[]
        visited=set()
        def dfs():
            if len(current)==len(nums):
                final.append(current.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                current.append(num)
                visited.add(num)
                dfs()
                val=current.pop()
                visited.remove(val)
        dfs()
        return final
            
                

            
                
            
            
            
                

        