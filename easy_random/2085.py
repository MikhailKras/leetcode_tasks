class Solution:
    def count(self, words: List[str]) -> dict:
        seen = {}
        for word in words:
            seen[word] = seen.get(word, 0) + 1
        return seen

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = 0
        common_words = set(words1) & set(words2)
        count1, count2 = self.count(words1), self.count(words2)
        for common_word in common_words:
            if count1[common_word] == 1 and count2[common_word] == 1:
                res += 1
        return res

