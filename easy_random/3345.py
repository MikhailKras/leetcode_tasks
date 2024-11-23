class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if reduce(lambda x, y: x * y, map(int, str(n))) % t == 0:
                return n
            n += 1
            
