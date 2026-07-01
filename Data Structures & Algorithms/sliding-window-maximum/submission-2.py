from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        max_list=[]
        i,j=0,k-1
        for m in range(k):
            if not dq:
                dq.append(m)
                continue
            while dq and nums[m]>=nums[dq[-1]]:
                dq.pop()
            dq.append(m)
        max_list.append(nums[dq[0]])
        while j<len(nums):
            i+=1
            j+=1
            if dq and dq[0]<i:
                dq.popleft()
            if j<len(nums):
                while dq and nums[j]>=nums[dq[-1]]:
                    dq.pop()
                dq.append(j)
                max_list.append(nums[dq[0]])
        return max_list
