class Solution:
    @staticmethod
    def get_diff_list(s: str) -> Tuple[int]:
        res = []
        for i in range(1, len(s)):
            res.append(ord(s[i]) - ord(s[i - 1]))
        return tuple(res)

    def oddString(self, words: List[str]) -> str:
        seen = {}
        word_dict = {}
        for word in words:
            diff_list = self.get_diff_list(word)
            seen[diff_list] = seen.get(diff_list, 0) + 1
            word_dict[diff_list] = word


        for key in seen:
            if seen[key] == 1:
                return word_dict[key]
                
