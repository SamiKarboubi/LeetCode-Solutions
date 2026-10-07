from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isvalid(s):
            balance = 0
            for c in s:
                if c.isalpha():
                    continue
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        valid_childrens = []
        queue = deque([s])
        visited = set()
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                children = queue.popleft()
                if children not in visited:
                    visited.add(children)
                    if isvalid(children):
                        valid_childrens.append(children)
                        continue
                    for i in range(len(children)):
                        if not children[i].isalpha():
                            queue.append(children[:i]+children[i+1:])
            if valid_childrens:
                return valid_childrens

        return [""]
        






                

                
            
                


