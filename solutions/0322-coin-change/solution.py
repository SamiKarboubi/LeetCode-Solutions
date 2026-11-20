from collections import deque
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        queue = deque([(amount,0)])
        visited = {amount}
        if amount == 0:
            return 0
        while queue:
            amount, level = queue.popleft()
            for coin in coins:
                nxt = amount - coin
                if nxt == 0:
                    return level + 1
                if nxt > 0 and nxt not in visited:
                    queue.append((nxt, level + 1))
                    visited.add(nxt)
        return -1
