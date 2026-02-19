class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            finale = []
            col = len(mat[0])
            row  = len(mat)
            for c in range(col):
                arr = []
                for r in range(row - 1, -1, -1):
                    arr.append(mat[r][c])
                finale.append(arr)
            return finale

        for i in range(4):
            mat = rotate(mat)
            if mat == target:
                return True
        return False

                


        








        # t , l = 0 , 0
        # b , r = len(mat) , len(mat[0])
        # arr = [[0] * r for _ in range(b)]
        # while t < b and l < r:
        #     for c in range(l , r):
        #         arr[c][r - 1] = mat[t][c]
        #     t += 1
        #     for k in range(t , b):
        #         arr[b - 1][k] = mat[k][r - 1]
        #     r -= 1
        #     for y in range(r - 1 , -1 , -1):
        #         arr[y][l] = mat[b - 1][y]
        #     b -= 1
        #     for o in range(b - 1, t - 1, - 1):
        #         arr[t][o] = mat[o][l]
        #     l += 1
        # return arr == target
        


        