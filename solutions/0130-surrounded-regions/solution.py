class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        marked = set()

        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0:
                return 
            if board[r][c] == "X" or (r,c) in marked:
                return
            marked.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == "O":
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in marked:
                    board[r][c] = "X"

        


        
        
