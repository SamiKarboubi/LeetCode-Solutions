class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s, current_s = sum(nums), 0
        for i in range(len(nums)):
            s -= nums[i]
            if s == current_s:
                return i
            current_s += nums[i]
        return -1
            

