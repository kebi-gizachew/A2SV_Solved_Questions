class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        sets = [(0,0),(0 , -1), (0 , 1), (-1, 0), (-1,1), (-1 , -1),(1, 0),(1,1),(1,-1)]
        arr =[[0]* col for r in range(row)]
        for i in range(row):
            for j in range(col):
                count = 0
                op = 0
                for n , m in sets:
                    if 0 <= i + n <row and 0 <= j + m < col:
                        count+=1
                        op += img[i + n][j + m]
                arr[i][j] = op // count
        return arr

                