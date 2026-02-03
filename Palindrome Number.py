class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        i=0
        j=len(y)-1
        while j>=i:
            if y[i]!=y[j]:
                return False
            j-=1
            i+=1
        return True
        
