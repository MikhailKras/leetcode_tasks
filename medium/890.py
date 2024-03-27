class Solution:
    @staticmethod
    def is_matching(word, pattern) -> bool:
        pattern_key = {}
        seen = set()
        for word_char, pattern_char in zip(list(word), list(pattern)):
            if word_char not in pattern_key:
                if pattern_char not in seen:
                    pattern_key[word_char] = pattern_char
                    seen.add(pattern_char)
                else:
                    return False
            elif pattern_key[word_char] != pattern_char:
                return False
        return True


    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if self.is_matching(word, pattern)]

