class Solution:
    def stringSequence(self, target: str) -> List[str]:
        target = list(target)
        cur = ["a"]
        res = []
        while cur != target:
            res.append("".join(cur))
            if cur[len(cur) - 1] == target[len(cur) - 1]:
                cur.append("a")
            else:
                cur[len(cur) - 1] = chr(ord(cur[len(cur) - 1]) + 1)
        else:
            res.append("".join(cur))
        return res

