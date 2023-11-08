class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eaten = 0
        types = set()
        i = 0
        n = len(candyType)
        while i < n and eaten < n // 2:
            if candyType[i] not in types:
                types.add(candyType[i])
                eaten += 1
            i += 1
        return len(types)

