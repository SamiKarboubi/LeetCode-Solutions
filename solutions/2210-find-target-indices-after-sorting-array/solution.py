class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result
