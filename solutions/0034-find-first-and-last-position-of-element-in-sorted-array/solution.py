class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        List=[]
        for i in range(len(nums)):
            if nums[i]== target:
                List.append(i)
        if not List:
            return [-1,-1]
        return [List[0],List[-1]]
        
