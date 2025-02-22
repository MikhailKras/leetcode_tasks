class Solution:
    @staticmethod
    def is_bad_pair(char1: str, char2: str) -> bool:
        if char1.lower() == char2.lower():
            if char1.islower() and char2.isupper():
                return True
            if char2.islower() and char1.isupper():
                return True
            return False
        return False

    def makeGood(self, s: str) -> str:
        stack = deque()
        for char in s:
            if stack and self.is_bad_pair(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

