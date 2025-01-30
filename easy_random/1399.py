class Solution:
    def countLargestGroup(self, n: int) -> int:
        seen = {}
        for num in range(1, n + 1):
            dsum = sum(map(int, str(num)))
            seen[dsum] = seen.get(dsum, 0) + 1
        return list(seen.values()).count(max(seen.values()))

