from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        count=0
        dq=deque()
        for i in range(n):
            if i in visited:
                continue
            count+=1
            visited.add(i)
            dq.append(i)
            while dq:
                node=dq.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dq.append(neighbor)
                        visited.add(neighbor)                    
            
        return count

        