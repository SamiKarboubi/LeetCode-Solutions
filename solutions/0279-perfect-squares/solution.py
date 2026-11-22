class Solution:
    def numSquares(self, n: int) -> int:
        psn = [k * k for k in range(1, int(n ** 0.5) + 1)]
        
        dp = [n] * (n+1)
        dp[0] = 0

        for a in range(1, n+1):
            for ps in psn:
                if ps > a:
                    break
                dp[a] = min(1+dp[a-ps], dp[a])

        return dp[n]


        

