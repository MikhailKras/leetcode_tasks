class Solution:
    def interpret(self, command: str) -> str:
        prev = command[0]
        res = prev if prev == "G" else ""
        for i in range(1, len(command)):
            prev = command[i - 1]
            if command[i] == "G":
                res += command[i]
            elif command[i] == ")":
                if prev == "(":
                    res += "o"
                elif prev == "l":
                    res += "al"
        return res

