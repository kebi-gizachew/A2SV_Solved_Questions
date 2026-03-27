class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [["."] * n for i in range(n)]
        result = []
        leftdia = set()
        rightdia = set()
        col = set()

        def trial(row):
            if row == n:
                result.append(["".join(i) for i in arr])
                return

            for k in range(n):
                if row + k in leftdia or row - k in rightdia or k in col:
                    continue
                arr[row][k] = "Q"
                col.add(k)
                leftdia.add(k + row)
                rightdia.add(row - k)
                trial(row + 1)
                arr[row][k] = "."
                col.remove(k)
                leftdia.remove(k + row)
                rightdia.remove(row - k)

        trial(0)
        return result
