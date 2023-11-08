https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/997654126/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)

        

        for i in range(n):
            cnt= 0
            for j in range(n):            
                    if nums[j] < nums[i]:
                        cnt += 1

                        
            output.append(cnt)
                        
                
        return output
