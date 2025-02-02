class Solution:
    def commonChars(self, words: List[str]) -> List[str]:        
        prev = None
        for word in words:
            seen = {}
            for char in word:
                seen[char] = seen.get(char, 0) + 1
            
            chars = list(seen.keys()).copy()
            for char in chars:
                if prev is not None:
                    if char in prev:
                        seen[char] = min(seen[char], prev[char])
                    else:
                        seen.pop(char)
            prev = seen
        
        res = []
        for char in prev:
            res += [char] * prev[char]
        return res
                
