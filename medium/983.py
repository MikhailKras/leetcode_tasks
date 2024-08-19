class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1] + 1
        dp = [0 for _ in range(max_day)]
        days_set = set(days)
        for i in range(1, max_day):
            dp[i] = dp[i - 1] if i not in days_set else min(
                dp[max(i - 1, 0)] + costs[0],
                dp[max(i - 7, 0)] + costs[1],
                dp[max(i - 30, 0)] + costs[2],
            )
        return dp[-1]

