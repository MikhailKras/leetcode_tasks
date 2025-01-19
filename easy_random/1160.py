class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            chars_copy = list(chars)
            for char in word:
                if char not in chars_copy:
                    break
                chars_copy.remove(char)
            else:
                res += len(word)
        return res

