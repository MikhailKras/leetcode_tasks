class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def get_neighbor_coords(x, y) -> List[Tuple]:
            left = (x, y - 1) if y - 1 >= 0 else None
            top = (x - 1, y) if x - 1 >= 0 else None
            right = (x, y + 1) if y + 1 < n else None  
            down = (x + 1, y) if x + 1 < m else None
            return [coords for coords in [left, top, right, down] if coords]
        
        def helper(cur, x, y, seen):
            if cur == word:
                return True
            seen.add((x, y))
            for new_x, new_y in get_neighbor_coords(x,y):
                new_word = cur + board[new_x][new_y]
                if word.startswith(new_word) and (new_x, new_y) not in seen:
                    if helper(new_word, new_x, new_y, seen):
                        return True
            seen.remove((x, y))

        for i in range(m):
            for j in range(n):
                if helper(board[i][j], i, j, set()):
                    return True
        return False

