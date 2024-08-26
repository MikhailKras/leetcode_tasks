class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for item in arr:
            seen[item] = seen.get(item, 0) + 1
        distincts = list(filter(lambda x: seen[x] == 1, seen))
        return "" if k > len(distincts) else distincts[k - 1]

