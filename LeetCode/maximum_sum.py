class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = 0
        col = 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        

        for row in range(m-2):
            for col in range(n-2):

                max_sum = sum(grid[row][col:col+3])+grid[row+1][col+1]+sum(grid[row+2][col:col+3])
                res = max(max_sum,res)




                
        return res
