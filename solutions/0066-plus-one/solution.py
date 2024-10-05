class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k=""
        for i in range(len(digits)):
            k=k+str(digits[i])
        k=int(k)
        k=k+1
        k=str(k)
        k=list(k)
        for i in range(len(k)):
            k[i]=int(k[i])
        return k
