import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        for point in points:
            distance.append(math.sqrt(point[0]**2+point[1]**2))
        heap=[]
        for item in zip(distance,points):
            heapq.heappush_max(heap,item)
        while len(heap)>k:
            heapq.heappop_max(heap)
        return [x[1] for x in heap]
