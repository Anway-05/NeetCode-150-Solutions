class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution=[]
        current=[]
        self.i=0
        def traverse(i):
            if i==len(nums):
                solution.append(current.copy())
                return
            current.append(nums[i])
            traverse(i+1)
            current.pop()
            traverse(i+1)
        traverse(0)
        return solution

