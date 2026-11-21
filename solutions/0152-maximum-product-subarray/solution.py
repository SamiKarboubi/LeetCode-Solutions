import math
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        ma, mi = 1, 1
        for num in nums:
            tmp = ma
            ma = max(num, num * ma, num * mi)
            mi = min(num, num * mi, num * tmp)
            res = max(ma, res)
        return res
