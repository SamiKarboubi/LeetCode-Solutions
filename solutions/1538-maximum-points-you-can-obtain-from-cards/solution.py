class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        l, r = 0, n - k
        total = sum(cardPoints[r:])
        res = total
        while r < n:
            total += (cardPoints[l] - cardPoints[r])
            res = max(res,total)
            l += 1
            r += 1

        return res
