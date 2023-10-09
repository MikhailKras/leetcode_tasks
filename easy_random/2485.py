class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        l, r = 1, n + 1
        while l < r:
            m = (l + r) // 2
            l_sum = m * (m - 1) // 2
            r_sum = total - l_sum - m
            if l_sum < r_sum:
                l = m + 1
            else:
                r = m
        return l if l * (l - 1) // 2 == total - l * (l + 1) // 2 else -1

