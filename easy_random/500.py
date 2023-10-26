class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = 'qwertyuiop'
        second = 'asdfghjkl'
        third = 'zxcvbnm'
        res = []
        check_row = first
        for word in words:
            if word[0].lower() in first:
                check_row = first
            elif word[0].lower() in second:
                check_row = second
            else:
                check_row = third
            for char in word[1:]:
                if char.lower() not in check_row:
                    break
            else:
                res.append(word)
        return res
                
