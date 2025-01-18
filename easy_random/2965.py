class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        res = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                else:
                    res.append(grid[i][j])
        res.append(n ** 2 * (1 + n ** 2) // 2 - sum(seen))
        return res
        
