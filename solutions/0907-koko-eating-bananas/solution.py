import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def canEat(mid):
            currH = 0
            for p in piles:
                currH += math.ceil(p / mid)
            return currH <= h

        while l <= r:
            mid = (l+r) // 2
            if canEat(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
