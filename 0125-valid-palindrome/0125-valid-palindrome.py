class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        # s.lower()
        stri=""
        for i in range(len(s)):
            if(a[i]>='a' and a[i]<='z' or (a[i]>='0' and a[i]<='9')):
                stri+=a[i]
            else:
                continue
        return (stri==stri[::-1])
        # i=0
        # j=len(stri)-1
        # c=1
        # while(i!=j):
        #     if(stri[i]==stri[j]):
        #         i+=1
        #         j-=1
        #         c=1
        #     else:
        #         c=0
        #         break
        # if(c):
        #     return True
        # else:
        #     return False