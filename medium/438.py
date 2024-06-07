class Solution:
    def counter(self, word: str) -> dict:
        seen = {}
        for char in word:
            seen[char] = seen.get(char, 0) + 1
        return seen

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        cur = s[:n]
        p_counter = self.counter(p)
        cur_counter = self.counter(cur)
        j = 0
        res = []
        for i in range(n, len(s)):
            if p_counter == cur_counter:
                res.append(j)
            cur_counter[cur[0]] -= 1
            if cur_counter[cur[0]] == 0:
                cur_counter.pop(cur[0])
            cur = cur[1:] + s[i]
            cur_counter[s[i]] = cur_counter.get(s[i], 0) + 1
            j += 1
        else:
            if p_counter == cur_counter:
                res.append(j)
        return res

