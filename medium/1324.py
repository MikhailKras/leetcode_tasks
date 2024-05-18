class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
        
        res = []
        for i in range(max_len):
            new_word = ''
            for word in words:
                if i > len(word) - 1:
                    new_word += ' '
                else:
                    new_word += word[i]
            res.append(new_word.rstrip())

        return res

