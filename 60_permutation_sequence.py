from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(list(permutations([f'{x}' for x in range(1, n+1)]))[k-1])
