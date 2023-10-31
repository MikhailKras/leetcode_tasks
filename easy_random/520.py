class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        first_is_upper, second_is_upper = word[0].isupper(), word[1].isupper()
        if not first_is_upper and second_is_upper:
            return False

        for char in word[2:]:
            if first_is_upper and second_is_upper:
                if char.islower():
                    return False
            elif (first_is_upper and not second_is_upper) or (not first_is_upper and not second_is_upper):
                if char.isupper():
                    return False
        return True
        
