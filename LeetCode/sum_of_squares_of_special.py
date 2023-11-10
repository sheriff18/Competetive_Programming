
https://leetcode.com/problems/sum-of-squares-of-special-elements/submissions/
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        cnt = []
        for i in range(0,len(nums)):
            if len(nums) % (i+1) == 0:
                cnt.append(nums[i])
        return sum([a**2 for a in cnt])
