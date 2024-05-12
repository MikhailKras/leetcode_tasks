class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        stack = [[0, [0]]]
        n = len(graph) - 1
        while stack:
            node, path = stack.pop()
            for neighbor in graph[node]:
                if neighbor == n:
                    res.append(path + [neighbor])
                else:
                    stack.append([neighbor, path + [neighbor]])
        return res

