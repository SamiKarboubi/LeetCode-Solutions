class Solution(object):
    def twoSum(self, nums, target):
       Output = []
       for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                Output.append(i)
                Output.append(j)
                return Output  

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
        
