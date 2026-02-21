class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dig = {"2": "abc","3": "def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        result = []
        n = len(digits)
        
        def helper(digits,digit):
            if len(digit) == n:
                result.append(digit)
                return
            for ltr in dig[digits[0]]:
                digit += ltr
                helper(digits[1:],digit)
                digit = digit[:-1]

        helper(digits,"")
        return result
                



        

