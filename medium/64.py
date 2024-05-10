class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        path_grid = [[float('inf') for _ in range(n)] for _ in range(m)]
        path_grid[0][0] = grid[0][0]

        for x in range(m):
            for y in range(n):
                if x - 1 >= 0 and y - 1 >= 0:
                    path_grid[x][y] = min(path_grid[x - 1][y], path_grid[x][y - 1]) + grid[x][y]
                elif x - 1 >= 0:
                    path_grid[x][y] = path_grid[x - 1][y] + grid[x][y]
                elif y - 1 >= 0:
                    path_grid[x][y] = path_grid[x][y - 1] + grid[x][y]
        return path_grid[-1][-1]

