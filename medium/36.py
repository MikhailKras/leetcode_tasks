class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_item(item: List[str]) -> bool:
            seen = set()
            for num in item:
                if num.isdigit():
                    if num in seen or not 1 <= int(num) <= 9:
                        return False
                    seen.add(num)
            return True

        for item in board:
            if check_item(item) is False:
                return False

        for item in zip(*board):
            if check_item(item) is False:
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                item = []
                for x in range(3):
                    for y in range(3):
                        item.append(board[i + x][j + y])
                if check_item(item) is False:
                    return False
        
        return True
                
