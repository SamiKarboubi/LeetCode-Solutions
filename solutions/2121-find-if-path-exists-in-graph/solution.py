from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        visited = set()
        to_visit = deque([source])
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        while to_visit:
            node = to_visit.popleft()
            if node == destination:
                return True
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    to_visit.append(child)

        return False
