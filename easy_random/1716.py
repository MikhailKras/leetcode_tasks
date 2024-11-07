class Solution:
    def totalMoney(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            if i % 7 == 0:
                dp[i] = dp[i - 7] + 1
            else:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

