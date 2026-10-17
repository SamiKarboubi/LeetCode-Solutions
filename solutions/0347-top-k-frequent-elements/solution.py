class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for freq in range(n, 0, -1):
            result.extend(buckets[freq])
            if len(result) >= k:
                break

        return result
