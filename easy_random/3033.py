class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_cols = {}
        n, m = len(matrix), len(matrix[0])
        cols = list(zip(*matrix))
        for i in range(m):
            max_cols[i] = max(cols[i])
        
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == -1:
                    matrix[row][col] = max_cols[col]
        
        return matrix
        
