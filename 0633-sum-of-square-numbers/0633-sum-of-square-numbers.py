class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        r = int(c ** (1/2))
        i = 0
        while r> i:
            t = i * i + r* r
            y = 2 * i* i
            x =2*r*r
            if  t== c or y ==c or x == c:
                return True
            elif t > c:
                r -= 1
            else:
                i += 1
        return False
            


        