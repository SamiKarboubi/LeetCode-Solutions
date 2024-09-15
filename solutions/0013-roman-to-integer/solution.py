class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        d=0
        for n in range(len(s)-1):
          if (roman[s[n]])  >= (roman[s[n+1]]):
            d=d+roman[s[n]]
          else:
            d=d-roman[s[n]]
        d=d+roman[s[-1]]
        return d

          
