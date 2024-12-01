class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        seen = {}
        n1, n2 = len(items1), len(items2)
        if n1 > n2:
            items2 += [None for _ in range(n1 - n2)]
        elif n2 > n1:
            items1 += [None for _ in range(n2 - n1)]
        for item1, item2 in zip(items1, items2):
            if item1:
                seen[item1[0]] = seen.get(item1[0], 0) + item1[1]
            if item2:
                seen[item2[0]] = seen.get(item2[0], 0) + item2[1]
        return [[value, weight] for value, weight in sorted(seen.items())]
        
