class Solution:
    def totalNQueens(self, n: int) -> int:
        leftD= set()
        col = set()
        rightD = set()
        arr = [[0] * n for i in range(n)]
        count= 0
        def trial(num , row):
            nonlocal count
            if row >= n:
                count+= 1
                return
            for i in range(n):
                if i + row in leftD or row - i in rightD or i in col:
                    continue
                leftD.add(i +row)
                rightD.add(row- i)
                col.add(i)
                trial(num , row + 1)
                leftD.remove(i + row)
                rightD.remove(row - i)
                col.remove(i)    
        trial(arr , 0)
        return count   