

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for j in t:
            if s.count(j) != t.count(j):
                return j
