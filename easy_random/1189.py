class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seen = {char: 0 for char in "balon"}
        for char in text:
            if char in seen:
                seen[char] += 1
        seen['l'] //= 2
        seen['o'] //= 2
        return min(seen.values())

