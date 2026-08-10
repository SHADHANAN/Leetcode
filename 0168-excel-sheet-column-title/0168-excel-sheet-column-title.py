class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a=[]
        while columnNumber>0:
            columnNumber-=1
            a.append(chr(columnNumber%26+ord('A')))
            columnNumber//=26
        return ''.join(reversed(a))
