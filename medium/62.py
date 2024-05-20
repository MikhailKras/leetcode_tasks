class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_len = m + n - 2
        return int(factorial(path_len)/factorial(m - 1)/factorial(n - 1))

