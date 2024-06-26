class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i - 1][j - (j == i)], triangle[i - 1][j - (j > 0)])
        return min(triangle[-1])

