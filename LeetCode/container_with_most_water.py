


https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) -1 
        result = 0
        
        while i < j:
            currArea = min(height[i],height[j]) * (j-i)
            result = max(result, currArea)
            if height[j] > height[i]:
                i+=1
            else:
                j-=1
        return result
        
        
