class Solution:
    def reverse(self,final):
        for i in range(len(final)//2):
            final[i],final[len(final)-i-1]=final[len(final)-i-1],final[i]
        return final
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
        visited=set()
        path=set()
        final=[]
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
            final.append(i)
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return self.reverse(final)

