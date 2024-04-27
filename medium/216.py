class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []

        def helper(cur_arr, i):
            if len(cur_arr) == k and sum(cur_arr) == n:
                res.append(cur_arr)
                return
            for j in range(i, 9):
                if sum(cur_arr) + digits[j] <= n:
                    helper(cur_arr + [digits[j]], j + 1)

        helper([], 0)
        return res

