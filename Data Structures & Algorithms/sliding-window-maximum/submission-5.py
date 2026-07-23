import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap=[]
        max_list=[]
        j=0
        while j<len(nums):
            heapq.heappush_max(max_heap,(nums[j],j))
            if j>=k-1:
                while max_heap[0][1]<=j-k:
                    heapq.heappop_max(max_heap)
                max_list.append(max_heap[0][0])
            j+=1
        return max_list
