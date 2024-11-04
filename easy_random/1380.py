class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins, col_maxs = {}, {}
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            row_mins[row] = min(matrix[row])

        for col in range(n):
            col_maxs[col] = max([matrix[row][col] for row in range(m)])
        
        res = []
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == row_mins[row] == col_maxs[col]:
                    res.append(matrix[row][col])
        return res

