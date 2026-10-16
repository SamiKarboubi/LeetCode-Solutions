class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {0:1}
        result = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            result += hash_table.get(current_sum - k, 0)
            hash_table[current_sum] = hash_table.get(current_sum, 0) + 1 
        return result
