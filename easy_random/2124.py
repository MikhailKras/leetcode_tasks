class Solution:
    def checkString(self, s: str) -> bool:
        id_a, id_b = s.rfind('a'), s.find('b')
        if id_a == -1 or id_b == -1:
            return True
        return id_a < id_b

