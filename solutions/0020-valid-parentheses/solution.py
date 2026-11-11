class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or c != pairs[stack.pop()]:
                    return False
        return not stack
