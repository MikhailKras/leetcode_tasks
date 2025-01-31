class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = {}
        for num in arr:
            seen[num] = seen.get(num, 0) + 1
        
        res = -1
        for key, val in seen.items():
            if key == val:
                res = max(key, res)
        return res
        
