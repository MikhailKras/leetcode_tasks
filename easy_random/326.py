class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return False if n <= 0 else not 3 ** 31 % n

