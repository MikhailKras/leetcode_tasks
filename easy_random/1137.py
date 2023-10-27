class Solution:
    def tribonacci(self, n: int) -> int:
        dn = [-1 for _ in range(n + 1)]
        dn[0] = 0
        if n >= 1:
            dn[1] = 1
        if n >= 2:
            dn[2] = 1
        if n >= 3:
            for i in range(3, n + 1):
                dn[i] = dn[i - 1] + dn[i - 2] + dn[i - 3]
        return dn[-1]
        
