class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(num ,times):
            res = 1
            while times > 0:
                if times % 2 == 1:
                    res *=num
                num *= num
                times //= 2
            return res
        if n < 0:
            x = 1/x
            n = -n
        return power(x , n)
        



        