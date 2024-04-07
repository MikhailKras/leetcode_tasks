class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_seen = {s[i]: i for i in range(n)}
        i, res = 0, []
        while i < n:
            end, j = last_seen[s[i]], i + 1
            while j < end:
                if last_seen[s[j]] > end:
                    end = last_seen[s[j]]
                j += 1
            res.append(end - i + 1)
            i = end + 1
        return res

