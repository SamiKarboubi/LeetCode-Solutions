from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = defaultdict(list)
        indegree = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for n_course in graph[course]:
                indegree[n_course] -= 1
                if indegree[n_course] == 0:
                    queue.append(n_course)

        return result if len(result) == numCourses else []

        

           
