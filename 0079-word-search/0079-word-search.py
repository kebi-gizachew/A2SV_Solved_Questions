class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # visited = set()
        directions = [(0 , -1), (-1 , 0), (0 ,1), (1 , 0)]
        def dfs(i , j, indx,visited):
            if indx == len(word):
                return True
            if i <0 or j<0 or i >=len(board) or j >= len(board[0]) or board[i][j] != word[indx] or (i , j) in visited:
                return False
            visited.add((i , j))
            for x , y in directions:
                if dfs(x + i , j + y, indx + 1, visited):
                    return True
            visited.remove((i , j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i , j, 0, set()):
                    return True
        return False


            



















        # visited = set()
        # def trial(i , j , idx):
        #     if idx == len(word):
        #         return True
                
        #     if i <0 or j <0 or i >= len(board) or j >= len(board[0]) or (i , j) in visited or board[i][j] != word[idx]:
        #         return False
        #     visited.add((i , j))
        #     temp = trial(i + 1 ,j , idx + 1) or trial(i - 1 , j , idx + 1) or trial(i , j + 1 , idx + 1) or trial(i , j -1 , idx + 1)
        #     visited.remove((i , j))
        #     return temp
            
        # temp = False
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         temp |= trial(i , j , 0)
        # return temp
        

            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna