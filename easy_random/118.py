from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[] for _ in range(numRows)]
        dp[0], dp[1] = [1], [1,1]
        for i in range(2, len(dp)):
            dp[i].append(1)
            for j in range(1, len(dp[i - 1])):
                dp[i].append(dp[i - 1][j] + dp[i - 1][j - 1])
            dp[i].append(1)
        return dp
