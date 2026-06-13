class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        index=0
        ans=[1 for _ in range(len(nums))]
        while i<index or j>index:
            if i<index:
                ans[index]*=nums[i]
                i+=1
            if j>index:
                ans[index]*=nums[j]
                j-=1
            if i==index and j==index and index<len(nums)-1:
                index+=1
                i=0
                j=len(nums)-1
        return ans