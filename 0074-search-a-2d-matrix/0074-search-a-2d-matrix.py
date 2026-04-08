class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bottom = 0 , len(matrix) - 1
        while bottom >= top:
            mid_vertical = top + (bottom - top) // 2
            if matrix[mid_vertical][0] <= target <= matrix[mid_vertical][-1]:
                left, right = 0 , len(matrix[0])
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[mid_vertical][mid] == target:
                        return True
                    elif matrix[mid_vertical][mid] > target:
                        right = mid - 1
                    else:
                        left= mid + 1
                return False
            elif matrix[mid_vertical][0] < target:
                top = mid_vertical + 1
            else:
                bottom = mid_vertical - 1
        return False




        