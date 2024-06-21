class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        seen = {}
        for word in words:
            seen[word] = seen.get(word, 0) + 1

        res = []
        for word in seen:
            if seen[word] == 1:
                res.append(word)
        return res

