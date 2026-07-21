import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            dist=point[0]**2+point[1]**2
            if len(heap)<k:
                heapq.heappush_max(heap,(dist,point))
            else:
                heapq.heappushpop_max(heap,(dist,point))
        return [x[1] for x in heap]
