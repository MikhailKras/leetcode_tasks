class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        def get_prev_vertex_value(x: int, y: int) -> int:
            vertexes = [matrix[x - 1][y]]
            if y - 1 >= 0:
                vertexes.append(matrix[x - 1][y - 1])
            if y + 1 < n:
                vertexes.append(matrix[x - 1][y + 1])
            return min(vertexes)

        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += get_prev_vertex_value(i, j)
        
        return min(matrix[-1])

