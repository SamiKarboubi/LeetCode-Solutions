class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=[]
        for num in nums:
            if num in unique:
                unique.remove(num)
            else:
                unique.append(num)
        return unique[0]

