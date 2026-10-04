class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1

            elif ch == ')':
                min_open -= 1
                max_open -= 1

            else:  # ch == '*'
                min_open -= 1   # si * = ')'
                max_open += 1   # si * = '('

            # Le minimum ne peut pas être négatif
            min_open = max(min_open, 0)

            # Même dans le meilleur cas, on a trop de ')'
            if max_open < 0:
                return False

        return min_open == 0
