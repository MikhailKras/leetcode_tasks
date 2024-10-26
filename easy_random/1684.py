class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                res += 1
        return res
        
