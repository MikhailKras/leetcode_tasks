class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        stack = [["", digits]]
        res = []
        seen = set()
        while stack:
            cur, remains = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            if len(cur) == 3:
                if int(cur) % 2 == 0:
                    res.append(int(cur))
                continue
            for i in range(len(remains)):
                if cur or remains[i] != 0:
                    stack.append([cur + str(remains[i]), remains[:i] + remains[i + 1:]])
        return sorted(res)

