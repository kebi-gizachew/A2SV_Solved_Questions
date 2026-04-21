class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        def fillBorder(i , j):
            nonlocal row , col
            if i < 0 or j <0 or i >= row or j >= col or board[i][j] != "O":
                return
            board[i][j] = "F"
            fillBorder(i + 1 , j)
            fillBorder(i -1 , j)
            fillBorder(i , j + 1)
            fillBorder(i , j -1)
        for i in range(row):
            for j in range(col):
                if (i == 0 or j == 0 or i == row - 1 or j == col - 1) and board[i][j] == "O":
                    fillBorder(i , j)
        for x in range(row):
            for y in range(col):
                if board[x][y] == "F":
                    board[x][y] = "O"
                elif board[x][y] == "O":
                    board[x][y] = "X"
        print(board)
        

        