class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums):
            if len(nums)== 1:
                return [nums[:]]
            perms=[]
            for i in range (len(nums)):
                for perm in backtrack(nums[:i]+nums[i+1:]):
                    perms.append(perm + [nums[i]])
            return perms
        return backtrack(nums)



        
