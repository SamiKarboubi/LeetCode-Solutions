class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1

        start = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if start == -1:
            return [-1,-1]
        end = -1

        left = start
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [start,end]


