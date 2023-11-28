class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        for row in range(rows):
            grid[row].sort(reverse=True)
        
        for col in range(cols):
            max_num = 0
            for row in range(rows):
                max_num = max(max_num, grid[row][col])
            res += max_num
        return res
        
