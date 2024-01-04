class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        s_dict = {}
        for word in s_list:
            s_dict[word[-1]] = word[:-1]
        res = []
        for num in range(1, len(s_list) + 1):
            res.append(s_dict[str(num)])
        return ' '.join(res)

