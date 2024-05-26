class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroes_x = set()
        zeroes_y = set()
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    zeroes_x.add(x)
                    zeroes_y.add(y)
        
        for x in zeroes_x:
            matrix[x] = list(map(lambda x: 0, matrix[x]))
        
        for y in zeroes_y:
            for x in range(m):
                matrix[x][y] = 0
        
