class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r + 1) // 2
            if (1 + m) * m // 2 <= n:
                l = m
            else:
                r = m - 1
        return l

