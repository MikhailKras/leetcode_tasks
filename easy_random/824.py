class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = []
        for i, word in enumerate(sentence.split()):
            cur = ""
            if word[0].lower() in vowels:
                cur += word + "ma"
            else:
                cur += word[1:] + word[0] + "ma"
            cur += "a" * (i + 1)
            res.append(cur)
        return " ".join(res)

