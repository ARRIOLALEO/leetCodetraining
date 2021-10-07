class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dc = {}
        size_matrix_row = len(mat)
        size_matrix_col = len(mat[0])
        
        for row in range(size_matrix_row):
            for col in range(size_matrix_col):
                if (row - col) in dc:
                    dc[row - col] += [mat[row][col]]
                else:
                    dc[row - col]  = [mat[row][col]]
        for d in dc:
            dc[d].sort()
        for row in range(size_matrix_row):
            for col in range(size_matrix_col):
                mat[row][col] = dc[row-col][0]
                del dc[row-col][0]
        return mat
            
