class Solution:
    def isFascinating(self, n: int) -> bool:
        return sorted(map(str, range(1, 10))) == sorted(list(str(n) + str(n * 2) + str(n * 3)))
            
