class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if k >= sum(diffs):
            return 0

        max_diff = max(diffs)
        counts = [0] * (max_diff + 1)

        for d in diffs:
            counts[d] += 1

        for i in range(max_diff, 0, -1):
            if k == 0:
                break

            reduce = min(counts[i], k)

            counts[i] -= reduce
            counts[i - 1] += reduce
            k -= reduce

        return sum(count * d**2 for d, count in enumerate(counts))

        












        return

