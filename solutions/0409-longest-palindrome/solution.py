class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        result = 0
        for car in s:
            d[car] = d.get(car, 0) + 1
            if d[car] % 2 == 0:
                result += 2

        return result if len(s) == result else result + 1
