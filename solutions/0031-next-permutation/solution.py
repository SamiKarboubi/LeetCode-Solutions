class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        perm_index = -1
        min_next = float("inf")
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                perm_index = i-1
                break

        if perm_index != - 1:
            for i in range(perm_index+1,n):
                if nums[i] <= min_next and nums[i] > nums[perm_index]:
                    min_next, min_next_index = nums[i], i
            nums[perm_index], nums[min_next_index] = nums[min_next_index], nums[perm_index]

        left, right = perm_index + 1 , n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
