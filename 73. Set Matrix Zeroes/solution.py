class Solution:
    def setZeroes(self, matrix: List[List[int]],) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        positions = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    positions.append([row,col])
        
        for ps in positions:
            row = ps[0]
            col = ps[1]
            
            for index in range(len(matrix[0])):
                matrix[row][index] = 0
            for index in range(len(matrix)):
                matrix[index][col] = 0
