class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost) + 1)]
        dp[0], dp[1] = 0, cost[0]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]
        return min(dp[-1], dp[-2])

