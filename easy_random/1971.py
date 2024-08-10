class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        stack = [source]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            if cur == destination:
                return True
            visited.add(cur)
            for neighbor in graph[cur]:
                stack.append(neighbor)
        
        return False

