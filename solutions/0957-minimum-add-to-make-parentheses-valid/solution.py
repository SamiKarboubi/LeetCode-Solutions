from collections import deque

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque([])
        score = 0
        for st in s:
            if st == '(':
                stack.appendleft(st)
            elif st == ')' and stack:
                stack.popleft()
            elif st ==')' and not stack:
                score += 1
        
        return len(stack) + score
