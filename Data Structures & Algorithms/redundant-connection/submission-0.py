from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(len(edges)+1)]
        def connected(u,v):
            dq=deque([u])
            visited={u}
            while dq:
                node=dq.popleft()
                for neighbor in graph[node]:
                    if neighbor==v:
                        return True
                    if neighbor not in visited:
                        dq.append(neighbor)
                    visited.add(neighbor)
        for u,v in edges:
            if connected(u,v):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)
        
