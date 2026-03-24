class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return None
        if x == 0:
            return 0
        N = 100
        a = x
        for _ in range(N):
            x = 0.5 * ( x + a / x)

        return int(x)
