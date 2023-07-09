

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))

        i = 0
        while i < 2*n:
            i = (i+k-1) % n
            if len(players) > 1:
                players.remove(players[i])
                n-=1
            else:
                return players[0]
