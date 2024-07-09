class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        seen = [False for _ in range(len(isConnected))]
        for node in range(len(isConnected)):
            if not seen[node]:
                queue = deque([node])
                while queue:
                    cur = queue.popleft()
                    seen[cur] = True
                    for neighbor in range(len(isConnected[cur])):
                        if isConnected[cur][neighbor] == 1 and not seen[neighbor]:
                            queue.append(neighbor)
                res += 1
        
        return res

