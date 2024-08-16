class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        cur = None
        while i + 2 < len(num):
            if not cur or int(num[i]) > cur:
                if num[i] == num[i + 1] == num[i + 2]:
                    cur = int(num[i])
                    i += 3
                else:
                    i += 1
            else:
                i += 1
        return "" if cur is None else str(cur) * 3

