class Solution:
    def fib(self, n: int) -> int:
        def last_fiban(x):
            if x == 1:
                return 1
            if x == 0:
                return 0
            return last_fiban(x - 1) + last_fiban(x - 2)
        return last_fiban(n)

        