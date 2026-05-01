class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1 , 0) , (1 , 0) , (0 , -1) , (0, 1)]
        def changeColor(i , j):
            nonlocal color
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == 1:
                image[i][j] = color
                for dirX, dirY in directions:
                    changeColor(dirX + i , dirY + j)
        changeColor(sr, sc)
        return image

        