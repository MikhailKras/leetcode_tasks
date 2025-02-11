class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cl, cr, c_ = 0, 0, 0
        for char in moves:
            match char:
                case "L":
                    cl += 1
                case "R":
                    cr += 1
                case "_":
                    c_ += 1
        return cl + c_ - cr if cl > cr else cr + c_ - cl
        
