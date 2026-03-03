class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def helper(act, op, cl):
            if op == n and cl == n:
                result.append(act)
                return

            if op < n:
                helper(act + "(", op + 1, cl)

            if cl < op:
                helper(act + ")", op, cl + 1)

        helper("", 0, 0)
        return result
