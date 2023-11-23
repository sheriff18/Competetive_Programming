https://leetcode.com/submissions/detail/1104597771/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        window_size = collections.Counter(s[:len(p)-1])
        cnt = []

        for i in range(len(p)-1, len(s)):
            window_size[s[i]] += 1
            if window_size == target:
                cnt.append(i-len(p)+1)
            
            if window_size[s[i-len(p)+1]] > 1:
                window_size[s[i-len(p)+1]] -= 1
            else:
                del window_size[s[i-len(p)+1]]
        return cnt
