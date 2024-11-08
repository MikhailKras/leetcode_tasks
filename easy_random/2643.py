class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        res = 0
        for i in range(len(mat)):
            cur = mat[i].count(1)
            if cur > max_ones:
                max_ones = cur
                res = i
        return [res, max_ones]

