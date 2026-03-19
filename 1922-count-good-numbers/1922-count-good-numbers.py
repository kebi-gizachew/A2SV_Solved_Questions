class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def p(num , times):
            res = 1
            while times >0:
                if times % 2 == 1:
                    res = (res * num) %(10**9 + 7)
                num = (num *num)% (10**9 + 7)
                times //= 2
            return res
        raises = ceil(n / 2)
        prime = n - raises
        return (p(5 , raises) * p(4 , prime)) % (10**9 + 7)
        
        