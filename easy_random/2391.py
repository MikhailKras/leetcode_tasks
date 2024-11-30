class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        lasts = {"M": -1, "G": -1, "P": -1}
        for i in range(len(garbage)):
            for key in lasts:
                if key in garbage[i]:
                    lasts[key] = i
        return sum(
            [sum(travel[:lasts[key]]) for key in lasts if lasts[key] != -1]
            ) + len("".join(garbage))

