class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        seen = {}
        freq = 0
        res = -1
        for num in nums:
            if num % 2 == 0:
                seen[num] = seen.get(num, 0) + 1
                if seen[num] > freq:
                    freq = seen[num]
                    res = num
                elif seen[num] == freq:
                    res = min(res, num)
        return res

