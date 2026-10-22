class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c):
            if r >= m or r < 0 or c >= n or c < 0 or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for di,dj in [(1,0),(0,1),(0,-1),(-1,0)]:
                area += dfs(r+di,c+dj)
            return area

        max_result = 0   
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    max_result = max(max_result,dfs(r,c))
        
        return max_result
