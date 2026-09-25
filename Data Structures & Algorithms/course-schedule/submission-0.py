class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
        visited=set()
        path=set()
        def dfs(i):
            if i in visited:
                return True
            path.add(i)
            for neighbor in graph[i]:
                if neighbor in path:
                    return False
                if not dfs(neighbor):
                    return False
            path.remove(i)
            visited.add(i)
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
