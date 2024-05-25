class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = set(wordDict)
        def helper(cur_list, cur_word, i):
            if i > len(s) - 1:
                if not cur_word:
                    res.append(' '.join(cur_list))
                return
            if cur_word + s[i] in words:
                helper(cur_list + [cur_word + s[i]], '', i + 1)
            helper(cur_list, cur_word + s[i], i + 1)
        
        helper([], '', 0)
        return res

