class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, num = coordinates[0], int(coordinates[1])
        if ord(letter) % 2 == 0:
            if num % 2 == 0:
                return False
            return True
        else:
            if num % 2 == 0:
                return True
            return False

