class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            i_left = nums[mid - 1] if mid - 1 != -1 else float("-inf")
            i_right = nums[mid + 1] if mid + 1 != n else float("-inf")
            
            if nums[mid] > i_left and nums[mid] > i_right:
                return mid
            if nums[mid] > i_right:
                right = mid 
            else:
                left = mid + 1
        
        
