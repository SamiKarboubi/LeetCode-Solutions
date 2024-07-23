class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        return s==s[::-1]
solution=Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))        
print(solution.isPalindrome(10))
