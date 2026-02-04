class Solution:    
    def findUnion(self, a, b):
        arr1=set(a)
        arr2=set(b)
        return sorted(arr1 | arr2)
            
        # code here
