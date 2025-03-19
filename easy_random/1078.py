class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text = text.split()
        for i in range(1, len(text) - 1):
            if (text[i - 1], text[i]) == (first, second):
                res.append(text[i + 1])
        return res
        
