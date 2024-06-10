class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        queue = [0]
        while queue:
            cur = queue.pop(0)
            if cur in seen:
                continue
            seen.add(cur)
            for room in rooms[cur]:
                queue.append(room)
        return len(seen) == len(rooms)
            
