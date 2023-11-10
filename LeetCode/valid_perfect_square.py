https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num**0.5 % 1 == 0:
            return True
        return False
