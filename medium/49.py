class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            word_sort = "".join(sorted(word))
            if word_sort not in seen:
                seen[word_sort] = [word]
            else:
                seen[word_sort].append(word)
        return seen.values()

