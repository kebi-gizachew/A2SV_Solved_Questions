class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        rs = rStart
        cs = cStart
        temp=  []
        temp.append([rs,cs])
        init = 1
        path = [(0 , 1) , (1,0), (0,-1),(-1,0)]
        while len(temp)<rows*cols:
            for i in range(4):
                k =init
                for m in range(k):
                    rs+=path[i][0]
                    cs+=path[i][1]
                    if 0<=rs<rows and 0<=cs<cols:
                        temp.append([rs,cs])
                        if len(temp) == rows*cols:
                            return temp
                if i%2 == 1:
                    init +=1
        return temp





        