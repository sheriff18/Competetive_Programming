https://leetcode.com/problems/percentage-of-letter-in-string/submissions/971255852/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return floor((s.count(letter)/ len(s))  * 100)
