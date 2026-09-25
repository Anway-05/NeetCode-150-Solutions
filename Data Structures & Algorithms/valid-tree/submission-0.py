from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dq=deque([(0,-1)])
        visited={0}
        while dq:
            node,root=dq.popleft()
            for neighbor in graph[node]:
                if neighbor==root:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                dq.append((neighbor,node))
        if len(visited)==n:
            return True
        else:
            return False
        