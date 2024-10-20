class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        res = 0
        while piles:
            piles.popleft()
            piles.pop()
            res += piles.pop()
        return res

