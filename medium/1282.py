class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in groups:
                groups[groupSizes[i]] = []
            groups[groupSizes[i]].append(i)
        
        res = []
        for size in groups:
            for i in range(0, len(groups[size]), size):
                res.append(groups[size][i:i + size])

        return res
        
