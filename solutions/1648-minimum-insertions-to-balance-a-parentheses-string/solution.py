class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        need = 0
        for c in s:
            if c == '(':
                if need % 2 == 1:
                    result += 1
                    need -= 1
                need += 2
            else:
                if need == 0:
                    result += 1
                    need += 2
                need -= 1

        return result + need
                
                    

        
        


