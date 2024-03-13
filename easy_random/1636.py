class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        res = []
        for num, freq in sorted(seen.items(), key=lambda x: (x[1], -x[0])):
            res.extend([num for _ in range(freq)])
        return res

