

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        length = len(s)
        
        while i < length:
            if i+2 < length and s[i+2] == '#':
                ans.append(chr(96+int(s[i:i+2])))
                i += 3
            else:
                ans.append(chr(96+int(s[i])))
                i += 1
        
        return ''.join(ans)
