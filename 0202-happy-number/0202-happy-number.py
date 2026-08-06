class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        ans=str(n)
        while int(ans)>1:
            if ans in seen:
                return False
            seen.add(ans)
            val=0
            for i in ans:
                val+=int(i)**2
            ans=str(val)
        return True
