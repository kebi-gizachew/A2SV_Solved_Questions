class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recur(x):
            if x == 1:
                return True
            if 0 <= x <1:
                return False
            return recur(x / 4)
        return recur(n)
        