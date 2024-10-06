class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        for i in range(len(s)-1):
            m=m+abs(ord(s[i])-ord(s[i+1]))
        return m
