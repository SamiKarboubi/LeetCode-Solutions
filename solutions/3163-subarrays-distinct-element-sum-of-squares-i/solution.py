class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = 0
        i = 0

        while i < n:
            j = i
            while j < n:
                total += len(set(nums[i:j+1])) ** 2
                j += 1
            i += 1

        return total
