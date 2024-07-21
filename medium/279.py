class Solution:
    def numSquares(self, n: int) -> int:
        res = 10 ** 6
        seen = {}
        def helper(cur_sum, count, num):
            nonlocal res
            if cur_sum > n:
                return
            if count >= res:
                return
            if cur_sum == n:
                res = min(res, count)
                return
            if (cur_sum, num) in seen and seen[(cur_sum, num)] < count:
                return
            seen[(cur_sum, num)] = count
            for i in range(int(n ** 0.5), num - 1, -1):
                helper(cur_sum + i ** 2, count + 1, i)
        
        helper(0, 0, 1)
        return res

