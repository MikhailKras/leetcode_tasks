class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = 0
        for command in commands:
            match command:
                case "DOWN":
                    res += n
                case "UP":
                    res -= n
                case "RIGHT":
                    res += 1
                case "LEFT":
                    res -= 1
        return res
        
