class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen_rows = {}
        for x in range(n):
            key = tuple(grid[x])
            seen_rows[key] = seen_rows.get(key, 0) + 1
        
        seen_cols = {}
        columns = list(zip(*grid))
        for x in range(n):
            key = tuple(columns[x])
            seen_cols[key] = seen_cols.get(key, 0) + 1
        
        res = 0
        for key in seen_rows:
            res += seen_rows[key] * seen_cols.get(key, 0)
        return res

