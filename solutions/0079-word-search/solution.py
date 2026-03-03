class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        self.result = False
        from collections import Counter
        
        board_count = Counter()
        for row in board:
            board_count += Counter(row)
        
        word_count = Counter(word)
        
        for ch in word_count:
            if word_count[ch] > board_count[ch]:
                return False
        def search(r,c,i):
            if i == len(word):
                self.result = True
                return
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] == "#":
                return
            if board[r][c] != word[i]:
                return
            p = board[r][c]
            board[r][c] = "#"
            search(r-1,c,i+1)
            search(r+1,c,i+1)
            search(r,c+1,i+1)
            search(r,c-1,i+1)
            board[r][c] = p


        for r in range(m):
            for c in range(n):
                if self.result:
                    break
                if board[r][c] == word[0]:
                    search(r,c,0)


        return self.result
