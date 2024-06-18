class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        res = 0
        words = text.split()
        for word in words:
            for char in word:
                if char in brokenLetters:
                    res += 1
                    break
        return len(words) - res


