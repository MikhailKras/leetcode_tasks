class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {str(key): set() for key in range(10)}
        for i in range(0, len(rings), 2):
            color, pos = rings[i], rings[i + 1]
            rods[pos].add(color)
        
        res = 0
        for pos in rods:
            if len(rods[pos]) == 3:
                res += 1
        
        return res
        
