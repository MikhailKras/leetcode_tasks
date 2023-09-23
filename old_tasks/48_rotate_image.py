import copy


class Solution:
    """
    Do not return anything, modify matrix in-place instead.
    """
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix_copy = copy.deepcopy(matrix)
        for i, row in enumerate(matrix):
            row.clear()
            for row_copy in matrix_copy:
                row.insert(0, row_copy[i])
