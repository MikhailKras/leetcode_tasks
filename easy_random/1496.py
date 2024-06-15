class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        pos = [0, 0]
        for item in path:
            match item:
                case "N":
                    pos[0] += 1
                case "S":
                    pos[0] -= 1
                case "E":
                    pos[1] += 1
                case "W":
                    pos[1] -= 1
            if tuple(pos) in seen:
                return True
            seen.add(tuple(pos))
        return False

