class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row , col = len(mat) , len(mat[0])
        finale = []
        flag = True
        for c in range(col):
            j = c
            i = 0
            arr = []
            while j >= 0 and i < row:
                arr.append(mat[i][j])
                i += 1
                j -= 1
            if flag:
                arr.reverse()
            finale.extend(arr)
            flag = not flag
        print(flag)
        for r in range(1 , row):
            i = r
            j = col - 1
            arr = []
            while j >= 0 and i < row:
                arr.append(mat[i][j])
                j -= 1
                i += 1
            if flag:
                arr.reverse()
            finale.extend(arr)
            flag = not flag
        return finale



                






        