class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0 for _ in range(min(n, 10))]
        dp[0] = 9
        for i in range(1, min(n, 10)):
            dp[i] = dp[i - 1] * (10 - i)
        return sum(dp) + 1

