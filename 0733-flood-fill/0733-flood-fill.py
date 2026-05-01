class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1 , 0) , (1 , 0) , (0 , -1) , (0, 1)]
        def changeColor(i , j, type1):
            nonlocal color
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == type1:
                image[i][j] = str(color)
                for dirX, dirY in directions:
                    changeColor(dirX + i , dirY + j, type1)
        changeColor(sr, sc, image[sr][sc])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == str(color):
                    image[i][j] = color
        return image

        