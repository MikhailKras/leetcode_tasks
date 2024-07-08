class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = {}
        for word in words2:
            cur_freq = {}
            for char in word:
                cur_freq[char] = cur_freq.get(char, 0) + 1
            
            for char in cur_freq:
                max_freq[char] = max(cur_freq[char], max_freq.get(char, 0))
        
        res = []
        for word in words1:
            seen = {}
            for char in word:
                seen[char] = seen.get(char, 0) + 1
            
            for char in max_freq:
                if char not in seen:
                    break
                if max_freq[char] - seen[char] > 0:
                    break
            else:
                res.append(word)
        
        return res
        
