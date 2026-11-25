import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))

        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        pq = [(0, k)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:          # entrée périmée
                continue
            for v, w in G[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        ans = max(dist.values())
        return ans if ans < float("inf") else -1
