class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, (rows*cols) -1

        while left <= right:
            mid = (right + left) // 2
            # use this formula to find exact indicies on 2-D matrix
            row, col = mid // cols, mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
            
            