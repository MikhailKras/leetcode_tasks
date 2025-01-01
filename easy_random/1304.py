class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for num in range(1, n // 2 + 1):
            res.extend([-num, num])
        if n % 2 == 1:
            res.append(0)
        return res
        
