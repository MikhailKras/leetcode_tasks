class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        dictionary.sort()
        for word in sentence.split():
            for dict_word in dictionary:
                if word.startswith(dict_word):
                    res.append(dict_word)
                    break
            else:
                res.append(word)
        return " ".join(res)

