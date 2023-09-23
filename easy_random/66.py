from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        num = str(num)
        return list(map(int, (''.join([num[i] + ' ' if i != len(num) else num[i]  for i in range(len(num))])).split()))
