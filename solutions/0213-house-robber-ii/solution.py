class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(lo, hi):
            prev, curr = 0, 0
            for i in range(lo, hi + 1):
                prev, curr = curr, max(curr, prev + nums[i])
            return curr

        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))
