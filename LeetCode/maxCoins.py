

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        len_arr = len(piles)
        answer = 0
        i = len_arr//3
        while i < len_arr:
            answer+=piles[i]
            i+=2
        return answer
