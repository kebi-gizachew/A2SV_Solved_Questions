class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col > row:
                    matrix[row][col], matrix[col][row] = matrix[col][row] , matrix[row][col]
        return matrix
        