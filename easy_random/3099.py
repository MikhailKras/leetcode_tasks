class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res = sum(map(int, list(str(x))))
        return res if x % res == 0 else -1

