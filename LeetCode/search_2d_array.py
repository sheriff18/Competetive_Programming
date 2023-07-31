
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False
