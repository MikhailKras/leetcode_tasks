from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        i, all_letters = 0, list(ascii_lowercase)
        key_dict = {}
        for char in key:
            if char.isalpha():
                if char not in key_dict:
                    key_dict[char] = ascii_lowercase[i]
                    i += 1
        res = []
        for char in message:
            res.append(key_dict.get(char, char))
        return ''.join(res)

