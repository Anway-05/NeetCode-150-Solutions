import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for task in tasks:
            freq[task]=freq.get(task,0)+1
        heap=[]
        for key,freq_task in freq.items():
            heapq.heappush_max(heap,(freq_task,key))
        dq=deque()
        time=0
        while heap or dq:
            time+=1
            while dq and dq[0][0]==time:
                ready_time,freq_task,task=dq.popleft()
                heapq.heappush_max(heap,(freq_task,task))
            if heap:
                freq_task,task=heapq.heappop_max(heap)
                if freq_task>1:
                    dq.append((time+n+1,freq_task-1,task))
        return time

            

        