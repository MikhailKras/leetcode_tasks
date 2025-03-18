class Solution:
    def minimumChairs(self, s: str) -> int:
        min_val = 0
        cur = 0
        for char in s:
            if char == "E":
                cur -= 1
                min_val = min(min_val, cur)
            else:
                cur += 1
        return -1 * min_val

