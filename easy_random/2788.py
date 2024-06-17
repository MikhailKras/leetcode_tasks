class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for item in words:
            res.extend([word for word in item.strip(separator).split(separator) if word])
        return res

