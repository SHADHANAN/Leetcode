class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=0
        t=word
        while t in sequence:
            k+=1
            t+=word
        return k