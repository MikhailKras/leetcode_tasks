class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def get_count_live_neighbors(x, y):
            res = 0
            for nx, ny in (
                [x - 1, y - 1],
                [x, y - 1],
                [x - 1, y],
                [x + 1, y + 1],
                [x, y + 1],
                [x + 1, y],
                [x + 1, y - 1],
                [x - 1, y + 1], 
            ):
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] in (1, 3):
                        res += 1
            return res
        for i in range(m):
            for j in range(n):
                count_live_neighbors = get_count_live_neighbors(i, j)
                if board[i][j] in (0, 2):
                    if count_live_neighbors == 3:
                        board[i][j] = 2
                else:
                    if count_live_neighbors < 2 or count_live_neighbors > 3:
                        board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        
