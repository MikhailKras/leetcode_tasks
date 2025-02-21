class Solution:
    def minimumPushes(self, word: str) -> int:
        seen = {num: [] for num in range(2, 10)}
        res = 0
        next_fill = 2
        for char in word:
            for key in range(2, 10):
                if char in seen[key]:
                    res += seen[key].index(char) + 1
                    break
            else:
                seen[next_fill].append(char)
                res += len(seen[next_fill])
                if next_fill == 9:
                    next_fill = 2
                else:
                    next_fill += 1
        return res


