class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        size_row = len(matrix)
        size_col = len(matrix[0])
        res = [[] for _ in range(size_col)]
        for row in range(size_row):
            for col in range(size_col):
                res[col].append(matrix[row][col])
        return res

