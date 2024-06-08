class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                s.pop(i)
                i -= 1
                if i >= 0:
                    if s[i].isalpha():
                        s.pop(i)
                        i -= 1
            i += 1
        
        return ''.join(s)
                
