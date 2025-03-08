class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            i = gifts.index(max(gifts))
            gifts[i] = int(gifts[i] ** 0.5)
            k -= 1
        return sum(gifts)

