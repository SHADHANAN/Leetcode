class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        a=n
        while True:
            prd=1
            for i in str(a):
                prd*=int(i)
            if(prd%t==0):
                return a
                break
            else:
                a+=1
            

        