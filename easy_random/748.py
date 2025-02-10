class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        seen = {}
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                seen[char] = seen.get(char, 0) + 1

        max_len = 1000
        res = ""
        for word in words:
            seen_copy = seen.copy()
            for char in word:
                if char.isalpha():
                    char = char.lower()
                    if char in seen_copy:
                        seen_copy[char] -= 1
            if all(x <= 0 for x in seen_copy.values()) is True:
                if len(word) < max_len:
                    max_len = len(word)
                    res = word
        return res
        
