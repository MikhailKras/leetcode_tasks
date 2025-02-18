class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set()
        special = set()
        for char in word:
            if char.islower():
                if char.upper() in seen:
                    special.add(char.lower())
            elif char.isupper():
                if char.lower() in seen:
                    special.add(char.lower())
            seen.add(char)
        return len(special)

