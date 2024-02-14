class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s, goal = list(s), list(goal)
        for _ in range(len(s)):
            if s == goal:
                return True
            s.append(s.pop(0))
        return False

