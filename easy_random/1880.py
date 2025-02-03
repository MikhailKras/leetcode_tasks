class Solution:
    @staticmethod
    def get_number(word: str) -> int:
        diff = 97
        res = ''
        for char in word:
            res += str(ord(char) - diff)
        return int(res)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.get_number(firstWord) + self.get_number(secondWord) == self.get_number(targetWord)
        
