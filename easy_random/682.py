class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for oper in operations:
            match oper:
                case "C":
                    res.pop()
                case "D":
                    res.append(res[-1] * 2)
                case "+":
                    res.append(res[-1] + res[-2])
                case _:
                    res.append(int(oper))
        return sum(res)

