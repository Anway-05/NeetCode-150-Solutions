class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stored=[]
        k=0
        while k<len(nums)-1:
            i,j=k+1,len(nums)-1
            while i<j:
                if nums[i]+nums[j]+nums[k] == 0:
                    stored.append([nums[i],nums[j],nums[k]])
                    while nums[i+1]==nums[i] and i<len(nums)-2:
                        i+=1
                    i+=1
                    while nums[j-1]==nums[j] and j>=2:
                        j-=1
                    j-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    j-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    i+=1
            while nums[k+1]==nums[k] and k<len(nums)-2:
                k+=1 
            k+=1
        return stored