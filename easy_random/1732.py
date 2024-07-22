class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        cur_alt = 0
        for i in gain:
            cur_alt += i
            max_alt = max(cur_alt, max_alt)
        return max_alt

