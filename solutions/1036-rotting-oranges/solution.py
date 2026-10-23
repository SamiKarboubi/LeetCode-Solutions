from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([])
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue:
            r, c, minutes = queue.popleft()
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = dr + r , dc + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr,nc,minutes+1))
                    fresh -= 1

        return minutes if fresh == 0 else -1
        
                    
