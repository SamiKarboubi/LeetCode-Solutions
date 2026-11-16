class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited  = set()
        res = 0
        def dfs(i):
            stack = [i]
            visited.add(i)
            while stack:
                i = stack.pop()
                for j in range(len(isConnected)):
                    if j not in visited and isConnected[i][j]:
                        stack.append(j)
                        visited.add(j)
                             
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res += 1
        return res
