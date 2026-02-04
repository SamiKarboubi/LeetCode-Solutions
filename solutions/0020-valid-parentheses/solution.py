class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                if pairs[stack.pop()] != c:
                    return False
        return not stack
