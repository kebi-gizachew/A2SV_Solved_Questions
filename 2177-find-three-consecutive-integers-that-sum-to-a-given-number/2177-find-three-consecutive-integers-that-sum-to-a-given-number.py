class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return []
        r=num//3
        g=[]
        g.extend([r-1,r,r+1])
        return g
        
        