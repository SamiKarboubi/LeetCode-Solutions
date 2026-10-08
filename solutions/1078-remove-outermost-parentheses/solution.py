class Solution:
    def removeOuterParentheses(self, s: str) -> str:
       
        n = len(s)
        balance = 0
        result = ""
        for j in range(n):
            if s[j] == '(':
                if balance != 0:
                    result += s[j]
                balance += 1
            else:
                balance -= 1
                if balance != 0:
                    result += s[j]

        return result
