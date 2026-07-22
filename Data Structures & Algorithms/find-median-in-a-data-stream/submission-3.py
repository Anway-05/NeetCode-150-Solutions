import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        self.count=0

    def addNum(self, num: int) -> None:
        self.count+=1
        heapq.heappush(self.min_heap,num)
        if len(self.min_heap)==len(self.max_heap)+2:
            heapq.heappush_max(self.max_heap,heapq.heappop(self.min_heap))
        elif self.max_heap and self.min_heap[0]<self.max_heap[0]:
                temp=self.min_heap[0]
                self.min_heap[0]=self.max_heap[0]
                self.max_heap[0]=temp

    def findMedian(self) -> float:
        if self.count%2==0:
            return float(self.max_heap[0]+self.min_heap[0])/2
        else:
            return float(self.min_heap[0])
        
        