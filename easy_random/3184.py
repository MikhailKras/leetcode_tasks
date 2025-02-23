class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        seen = {}
        res = 0
        for item in hours:
            item = item % 24
            if 24 - item in seen:
                res += seen[24 - item]
            elif item == 0 and 0 in seen:
                res += seen[item]
            seen[item] = seen.get(item, 0) + 1
        return res

