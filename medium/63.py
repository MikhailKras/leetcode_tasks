class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y] != 1 and (x, y) != (0, 0):
                    top, left = 0, 0
                    if x - 1 >= 0:
                        top = dp[x - 1][y]
                    if y - 1 >= 0:
                        left = dp[x][y - 1]
                    dp[x][y] = top + left
        return dp[-1][-1]

