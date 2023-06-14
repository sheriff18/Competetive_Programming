https://leetcode.com/problems/merge-strings-alternately/submissions/971282317/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1),len(word2))
        result = ''
        for i in range(length):
            result += word1[i] + word2[i]
        
        if len(word1) > length:
            result += word1[length:]
        
        elif len(word2) > length:
            result += word2[length:]
        
        return result
