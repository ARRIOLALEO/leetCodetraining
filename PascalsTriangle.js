class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]
        if numRows == 1:
            return solution
        for row in range(1,numRows):
            parcial = [1]
            counter = 1
            while counter < row:
                parcial.append(solution[row - 1][counter - 1] + solution[row - 1][counter])
                counter += 1
            parcial.append(1)
            solution.append(parcial)
        return solution
