https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen  = {}
        start = 0
        length = 0

        for end in range(len(s)):
            char = s[end]
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            else: 
                length = max(length, end- start +1)
            seen[char] = end
        return length
