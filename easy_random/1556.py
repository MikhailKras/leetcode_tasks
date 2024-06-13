class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n))
        for i in range(len(n) - 4, -1, -3):
            n[i] = n[i] + '.'
        return ''.join(n)

