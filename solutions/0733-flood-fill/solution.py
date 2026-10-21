class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        d_color = image[sr][sc]

        if d_color == color:
            return image

        def dfs(r,c):
            if r >= m or r < 0 or c >= n or c < 0:
                return
            if image[r][c] != d_color:
                return
            image[r][c] = color
            for di,dj in [(1,0),(0,1),(0,-1),(-1,0)]:
                dfs(r+di,c+dj)
            
        dfs(sr,sc)

        return image
