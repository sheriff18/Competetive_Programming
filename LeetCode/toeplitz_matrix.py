
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(1,len(matrix)):
            
            for col in range(1,len(matrix[0])):
                top_left = matrix[row-1][col-1]
                
                if matrix[row][col] != top_left:
                    return False
        return True
