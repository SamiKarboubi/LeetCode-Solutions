class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10: 
            f = 0
            p = num
            while p > 0: 
                f += p % 10  
                p //= 10  
            num = f  
        return num 
    
