class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]<=nums[r]:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                if target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                if nums[l]<=nums[m]:
                    if target>=nums[l] and target<nums[m]:
                        r=m-1
                    else:
                        l=m+1
                else:
                    if target<=nums[r] and target>nums[m]:
                        l=m+1
                    else:
                        r=m-1

        return -1
                