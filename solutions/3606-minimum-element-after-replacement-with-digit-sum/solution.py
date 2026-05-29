class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        min_c = float('inf')
        for i in range(len(nums)):
            st = 0
            for c in str(nums[i]):
                st += int(c)
            min_c = min(min_c,st)

        return min_c
        
