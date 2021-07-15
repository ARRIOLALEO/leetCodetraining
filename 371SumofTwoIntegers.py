class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        both_negative = False
        if a < 0 and b < 0:
            both_negative = True
            a = a * -1
            b = b * -1
        if a > 0 and b > 0:
            solution = []
            for i in range(a):
                solution.append("0")
            for j in range(b):
                solution.append("0")
            if both_negative:
                return len(solution) * -1
            else:
                return len(solution)

        if a < 0 or b < 0:
            if b > (a * -1):
                solution = []
                for i in range(b):
                    solution.append("0")
                for i in range(a * -1):
                    solution.pop(0)
                return len(solution)
            else:
                solution = []
                for i in range(a):
                    solution.append("0")
                for i in range(b * -1):
                    solution.pop(0)
                return len(solution) * -1
