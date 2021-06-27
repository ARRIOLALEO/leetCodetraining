class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = coordinates[0]
        row = coordinates[1]
        if (ord(col) -60) % 2 == 0:
            if int(row) % 2 == 0:
                return False
            else:
                return True
        else:
            if int(row) % 2 == 0:
                return True
            else:
                return False
