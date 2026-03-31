class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col = [set() for i in range(9)]
        row = [set() for i in range(9)]
        diagonal = [set() for i in range(9)]
        res = []
        void = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                b= board[i][j]
                if b != ".":
                    col[j].add(int(b))
                    row[i].add(int(b))
                    temp = (i // 3) * 3 + (j // 3)
                    diagonal[temp].add(int(b))
                else:
                    temp = (i // 3) * 3 + (j // 3)
                    void.append((i , j , temp))
        def trial(board ,a):
            if a == len(void):
                return True
            (i , j , z) = void[a]
            for k in range(1 , 10):
                if k not in col[j] and k not in row[i] and k not in diagonal[z]:
                    board[i][j] = str(k)
                    col[j].add(k)
                    row[i].add(k)
                    diagonal[z].add(k)
                    if trial(board , a + 1):
                        return True
                    board[i][j] = "."
                    col[j].remove(k)
                    row[i].remove(k)
                    diagonal[z].remove(k)
            return False
                
        trial(board , 0)
        








        #     if len(void) == a or r == len(board):
        #         return True
        #     for i in range(len(board[0])):
        #         if board[r][i] != ".":
        #             continue
        #         for j in range(1 , 9):
        #             d = (r // 3) * 3 + (i // 3)
        #             if j not in col[i] and j not in row[r] and j not in diagonal[d]:
        #                 board[r][i] = str(j)
        #                 col[i].add(j)
        #                 row[r].add(j)
        #                 diagonal[d].add(j)
        #                 if trial(board , r + 1 , a + 1):
        #                     return True                        
        #                 board[r][i] = "."
        #                 col[i].remove(j)
        #                 row[r].remove(j)
        #                 diagonal[d].add(j)
        # return trial(board, 0 , 0)
                





        
        
        