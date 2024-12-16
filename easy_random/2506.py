class Solution:
    def similarPairs(self, words: List[str]) -> int:
        seen = {}
        for word in words:
            cur = tuple(sorted(set(word)))
            seen[cur] = seen.get(cur, 0) + 1
        return sum([(x * (x - 1)) // 2 for x in seen.values()])

