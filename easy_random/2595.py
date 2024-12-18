class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bin_num = bin(n)[2:]
        even, odd = 0, 0
        for i, rev_i in zip(range(len(bin_num) - 1, -1, -1), range(len(bin_num))):
            if bin_num[i] == "1":
                if rev_i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]

