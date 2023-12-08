class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct = {}
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False

        for p, word in zip(pattern, s_list):
            if p not in dct:
                if word in dct.values():
                    return False
                dct[p] = word
            else:
                if dct[p] != word:
                    return False
        return True

