class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums):
            if len(nums)== 1:
                return [nums[:]]
            perms=[]
            seen=[]
            for i in range (len(nums)):
                if nums[i] not in seen:
                    seen.append(nums[i])
                    for perm in backtrack(nums[:i]+nums[i+1:]):
                        perms.append(perm + [nums[i]])
            return perms
        return backtrack(nums)
