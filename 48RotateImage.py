def inverse(matrix):
    len_matrix = len(matrix)
    for i in range(len_matrix):
        for j in range(floor(len_matrix / 2)):
            [matrix[i][j], matrix[i][len_matrix - j - 1]] = [
                matrix[i][len_matrix - j - 1],
                matrix[i][j],
            ]
    return matrix


def flip(matrix):
    len_matrix = len(matrix)
    for i in range(len_matrix):
        for j in range(len_matrix - i):
            [matrix[i][j], matrix[len_matrix - j - 1][len_matrix - i - 1]] = [
                matrix[len_matrix - j - 1][len_matrix - i - 1],
                matrix[i][j],
            ]
    return matrix


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        inverse(matrix)
        flip(matrix)
