class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(map(ord, s1)), sorted(map(ord, s2))
        res = [x - y for x, y in zip(s1, s2)]
        pos, neg = None, None
        for num in res:
            if num > 0:
                pos = num
            elif num < 0:
                neg = num
        return not (pos and neg) 

