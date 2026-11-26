import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        
        n, m = len(heights), len(heights[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]
        while pq:
            effort, i, j = heapq.heappop(pq)
            if effort > dist[i][j]:
                continue
            if (i, j) == (n-1, m-1): 
                return effort
            for di, dj in [(0, -1), (1, 0), (-1, 0), (0, 1)]:
                new_i, new_j = i + di, j + dj
                if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                    continue
                new_effort = max(dist[i][j], abs(heights[i][j] - heights[new_i][new_j]))
                if dist[new_i][new_j] > new_effort:
                    heapq.heappush(pq, (new_effort, new_i, new_j))
                    dist[new_i][new_j] = new_effort

        return dist[n-1][m-1]

