class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True
        #code here
