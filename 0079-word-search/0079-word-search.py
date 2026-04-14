class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def trial(i , j , idx):
            if idx == len(word):
                return True
                
            if i <0 or j <0 or i >= len(board) or j >= len(board[0]) or (i , j) in visited or board[i][j] != word[idx]:
                return False
            visited.add((i , j))
            temp = trial(i + 1 ,j , idx + 1) or trial(i - 1 , j , idx + 1) or trial(i , j + 1 , idx + 1) or trial(i , j -1 , idx + 1)
            visited.remove((i , j))
            return temp
            
        temp = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp |= trial(i , j , 0)
        return temp
        

            
        