class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col =len(matrix[0])
        finale = [[0] * row for _ in range(col)]
        for r in range(len(finale)):
            for c in range(len(finale[0])):
                finale[r][c] = matrix[c][r]
        return finale
        