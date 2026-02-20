class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        n = len(nums)
        def helper(nums,permutation):

            if len(permutation) == n:
                permutations.append(permutation.copy())
                return 
            for i in range(len(nums)):
                permutation.append(nums[i]) 
                helper(nums[:i]+nums[i+1:],permutation)
                permutation.pop()

        helper(nums,[])

        return permutations



