class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        S = sum(nums)
        if S % 2 != 0 or len(nums) == 1:
            return False
        target = S // 2
        set_sum = {0}
        for num in nums:
            set_sum_list = set()
            for val in set_sum:
                if val + num <= target:
                    set_sum_list.add(val + num)
            set_sum |= set_sum_list
            if target in set_sum:
                return True
        return False
