class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        check_set = set(range(1, n + 1))
        for row in matrix:
            if set(row) != check_set:
                return False
        
        for col in zip(*matrix):
            if set(col) != check_set:
                return False
        
        return True
        
