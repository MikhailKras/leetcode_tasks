class Solution:
    def getLucky(self, s: str, k: int) -> int:
        diff = 96
        s = "".join([str(ord(char) - 96) for char in s])
        while k:
            s = str(sum(map(int, s)))
            k -= 1
        
        return int(s)

