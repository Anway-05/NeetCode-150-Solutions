from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        dq=deque()
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                dq.append(i)
        final=[]
        while dq:
            node=dq.popleft()
            final.append(node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    dq.append(neighbor)
        if len(final)==len(indegree):
            return final
        else:
            return []
