class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat)
        for i in range(n):
            for j in range(n):
                if i == j:
                    res += mat[i][j]
                elif i + j == n - 1:
                    res += mat[i][j]
        return res

