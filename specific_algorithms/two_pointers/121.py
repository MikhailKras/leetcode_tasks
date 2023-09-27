from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                res = max(res, diff)
            else:
                l = r
            r += 1
        return res
