class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        r = int(c ** (1/2))
        i = 0
        while r> i:
            t = i * i + r* r
            if  t== c:
                return True
            elif t > c:
                r -= 1
            else:
                i += 1
        return False
            


        