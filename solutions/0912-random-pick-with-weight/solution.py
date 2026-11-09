import random
class Solution:

    def __init__(self, w: list[int]):
        self.n = len(w)
        self.w_sum = [w[0]] * self.n
        for i in range(1,self.n):
            self.w_sum[i] = (w[i]) + self.w_sum[i-1]

    def pickIndex(self) -> int:
        p = random.randint(1, self.w_sum[-1])
        l, r = 0, self.n - 1
        while l < r:
            mid = (l+r) // 2
            if self.w_sum[mid] >= p:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
