class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1 = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r == c:
                   sum1 += mat[r][c]
                elif r + c == len(mat) - 1 :
                    sum1 += mat[r][c]

        return(sum1)
