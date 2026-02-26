from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for (A,B),val in zip(equations,values):
            graph[A].append((B,val))
            graph[B].append((A,1/val))
            graph[A].append((A,1))
            graph[B].append((B,1))
        
        result = []

        def dfs(A,B,value,visited):
            if A == B:
                return value
             
            visited.add(A)
            for neighbor,weight in graph[A]:
                if neighbor not in visited:
                    res = dfs(neighbor,B,value*weight,visited)
                    if res != -1:
                        return res
            return -1

        for (A,B) in queries:
            if A not in graph or B not in graph:
                result.append(-1.0)
            else:
                visited = set()
                result.append(dfs(A, B, 1.0, visited))

        return result
