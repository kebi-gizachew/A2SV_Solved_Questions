class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            flag=False
            for j in range(len(matrix[0])):
                if flag==True and matrix[i][j]!=0:
                    matrix[i][j]=0.5
                if matrix[i][j]==0:
                    flag=True
        for i in range(len(matrix)):
            flag=False
            for j in range(len(matrix[0])-1,-1,-1):
                if flag==True and matrix[i][j]!=0:
                    matrix[i][j]=0.5
                if matrix[i][j]==0:
                    flag=True
        for j in range(len(matrix[0])):
            flag=False
            for i in range(len(matrix)):
                if flag==True and matrix[i][j]!=0:
                    matrix[i][j]=0.5
                if matrix[i][j]==0:
                    flag=True
        for j in range(len(matrix[0])):
            flag=False
            for i in range(len(matrix)-1,-1,-1):
                if flag==True and matrix[i][j]!=0:
                    matrix[i][j]=0.5
                if matrix[i][j]==0:
                    flag=True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0.5:
                    matrix[i][j]=0
        return matrix


