#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        from collections import Counter
        t=Counter(a)
        for i in b:
            if i not in t or t[i]==0:
                return False
            t[i]-=1
        return True
            
        # Your code here
    
    
    
    
