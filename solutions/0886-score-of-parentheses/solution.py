class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        var = 0
        score = 1
        prev_score = 0
        app = False
        for st in s:
            if st == '(':
                var += 1
                app = False
            elif st == ')':
                if not app:
                    if var > 1:
                        score = 2**(var - 1)
                    app = True
                    score += prev_score
                    prev_score = score
                    score = 1
                var -= 1

        return prev_score

