class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return list(filter(lambda num: x in words[num], range(len(words))))

