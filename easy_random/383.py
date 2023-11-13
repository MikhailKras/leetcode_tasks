class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n, m = len(ransomNote), len(magazine)
        if n > m:
            return False
        dct = {}
        for i, j in zip(ransomNote + ' ' * (m - n), magazine):
            if i != ' ':
                dct[i] = dct.get(i, 0) - 1
            dct[j] = dct.get(j, 0) + 1
        print(dct)
        return all(num >= 0 for num in dct.values())

