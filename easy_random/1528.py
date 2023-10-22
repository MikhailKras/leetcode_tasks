class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['' for _ in range(len(s))]
        for place, char in zip(indices, s):
            res[place] = char
        return ''.join(res)
        
