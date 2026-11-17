class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        S = sum(stones)
        if len(stones) == 1:
            return stones[0]
        target, m = S // 2, float('inf')
        set_sum = {0}
        for stone in stones:
            set_sum_list = set()
            for val in set_sum:
                current_val = val + stone
                if current_val <= target:
                    set_sum_list.add(current_val)
                    m = min(m, abs(S - 2*current_val))
            set_sum |= set_sum_list
        return m
