class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set()
        res = ""
        for char in s:
            if char.islower():
                if char.upper() in seen:
                    if not res or ord(res) < ord(char.upper()):
                        res = char.upper()
            elif char.isupper():
                if char.lower() in seen:
                    if not res or ord(res) < ord(char):
                        res = char.upper()
            seen.add(char)
        return res

