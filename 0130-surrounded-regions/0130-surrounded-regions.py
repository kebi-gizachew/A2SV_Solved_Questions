class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        def trial(i , j):
            if i + 1 >= row or j + 1 >= col or i - 1 < 0 or j -1 <0 or board[i][j] == "X":
                return
            board[i][j] = "X"
            trial(i + 1 , j)
            trial(i - 1 , j)
            trial(i , j + 1)
            trial(i , j - 1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    trial(i , j)
    

        