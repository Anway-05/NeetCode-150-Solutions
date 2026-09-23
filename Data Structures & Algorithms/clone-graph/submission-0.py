"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dq=deque([node])
        old_to_new={node:Node(node.val)}
        while dq:
            n=dq.popleft()
            for neighbor in n.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor]=Node(neighbor.val)
                    dq.append(neighbor)
                old_to_new[n].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]
        