class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = -1
        for sentence in sentences:
            max_words = max(max_words, len(sentence.split()))
        return max_words
        
