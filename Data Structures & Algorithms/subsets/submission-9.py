class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution=[]
        current=[]
        self.i=0
        def traverse(i):
            solution.append(current.copy())
            for j in range(i,len(nums)):
                current.append(nums[j])
                traverse(j+1)
                current.pop()
        traverse(0)
        return solution

