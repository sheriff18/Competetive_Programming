class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={c:i for i,c in enumerate(order)}
        prev=list(dic[char] for char in words[0])
        for i in range(1,len(words)):
            cur=list(dic[ch] for ch in words[i])
            if cur<prev:
                return False
            prev=cur
        return True
        
         
