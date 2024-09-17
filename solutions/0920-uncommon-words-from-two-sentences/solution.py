class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        l1=[]
        s11=s1.split()
        s22=s2.split()
        s11.extend(s22)
        for word in s11:
            if s11.count(word) == 1:
                l1.append(word)
        return l1



