class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph_dict = {node: 0 for node in range(1, len(edges) + 2)}
        for edge in edges:
            graph_dict[edge[0]] += 1
            graph_dict[edge[1]] += 1
        for node in graph_dict:
            if graph_dict[node] == len(edges):
                return node

