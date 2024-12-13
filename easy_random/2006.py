class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        used = set()
        res = 0
        for num in seen:
            if num not in used:
                used.add(num)
                if num - k in seen:
                    res += seen[num] * seen[num - k]
                if num + k in seen:
                    res += seen[num] * seen[num + k]
        return res // 2

