class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n+1))
        result = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a,b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                result = [a,b]
            else:
                parent[ra] = rb
        return result
