class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        cur_seen = set()
        while r < len(s):
            if s[r] not in cur_seen:
                cur_seen.add(s[r])
            else:
                max_len = max(r - l, max_len)
                old_l = l
                l = s.find(s[r], old_l) + 1
                for i in range(old_l, l):
                    if s[i] in cur_seen:
                        cur_seen.remove(s[i])
                cur_seen.add(s[r])
            r += 1
        return max(max_len, r - l)
            
