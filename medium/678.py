class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterisk_ids = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                elif asterisk_ids:
                    asterisk_ids.pop()
                else:
                    return False
            else:
                asterisk_ids.append(i)

        while stack and asterisk_ids:
            if asterisk_ids[-1] > stack[-1]:
                stack.pop()
                asterisk_ids.pop()
            else:
                return False

        return len(stack) == 0

