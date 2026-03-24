class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        n = x    
        result = 0
        while x != 0:
            result *= 10
            result += x % 10
            x = x // 10
        return result == n

        
