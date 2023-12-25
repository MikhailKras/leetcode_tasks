class Solution:
    def fib(self, n: int) -> int:
        dn = [0, 1, 1]
        if n < 3:
            return dn[n]
        for _ in range(3, n + 1):
            dn[0], dn[1] = dn[1], dn[2]
            dn[2] = dn[0] + dn[1]
        return dn[-1]

