import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(string.ascii_lowercase)
        for char in sentence:
            if char.isalpha():
                if char.lower() in letters:
                    letters.remove(char.lower())
                    if not letters:
                        return True
        return False

