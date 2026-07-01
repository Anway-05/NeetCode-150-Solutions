class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j=0,k-1
        max_list=[]
        stack=[]
        for m in range(k):
            if not stack:
                stack.append(m)
                continue
            while stack and nums[m]>=nums[stack[-1]]:
                stack.pop()
            stack.append(m)
        max_list.append(nums[stack[0]])
        x=0
        while j<len(nums)-1:
            j+=1
            i+=1
            while stack and nums[j]>=nums[stack[-1]]:
                stack.pop()
            stack.append(j)
            while x<len(stack) and stack[x]<i:
                x+=1
            if x==len(stack):
                stack=[j]
                x=0
            max_list.append(nums[stack[x]])
        return max_list


