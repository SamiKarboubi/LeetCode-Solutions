class Solution(object):
    def isValid(self, s):
        stack=[]
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == '{':
                stack.append(p)
            elif p == '[':
                stack.append(p)
            elif p == ')':
                if '(' not in stack:
                    return False
                elif stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif p == ']':
                if '[' not in stack:
                    return False
                elif stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif p == '}':
                if '{' not in stack:
                    return False
                elif stack[-1] != '{':
                    return False
                else:
                    stack.pop() 
        return True if stack==[] else False
