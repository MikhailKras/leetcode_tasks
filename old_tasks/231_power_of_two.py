class Solution:
    def isPowerOfTwo(self, n) -> bool:
        new_n = n / 2
        if new_n == 1 or n == 1:
            return True
        if new_n != n // 2 or n == 0:
            return False
        return self.isPowerOfTwo(new_n)
