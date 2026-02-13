class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l , r = 0 , len(matrix[0])
        t , b = 0 , len(matrix)
        arr = []
        while r > l and b > t:
            for c in range(l , r):
                arr.append(matrix[t][c])
            t += 1
            for n in range(t , b):
                arr.append(matrix[n][r - 1])
            r -= 1
            if not (l < r and t < b):
                break
            if r > l:
                for y in range(r - 1 , l - 1 , -1):
                    arr.append(matrix[b - 1][y])
            b -= 1
            if b > t:
                for h in range(b - 1 , t - 1 , -1):
                    arr.append(matrix[h][l])
            l += 1
        return arr

        