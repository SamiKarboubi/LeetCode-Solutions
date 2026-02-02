class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        longest = 0

        for num in set_nums:
            if num - 1 not in set_nums:   
                current = num
                length = 1

                while current + 1 in set_nums:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
