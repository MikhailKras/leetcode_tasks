class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end_word = len(s) - 1
        while end_word >= 0 and s[end_word] == ' ':
            end_word -= 1

        c = end_word
        count = 0
        while c >= 0 and s[c] != ' ':
            count += 1
            c -= 1
        return count
        
