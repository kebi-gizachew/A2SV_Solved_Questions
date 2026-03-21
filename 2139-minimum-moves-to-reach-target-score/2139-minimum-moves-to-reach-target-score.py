class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        def trial(res):
            nonlocal count , maxDoubles
            if res == 1:
                return
            if res % 2== 0 and maxDoubles != 0:
                maxDoubles -= 1
                count += 1
                trial(res // 2)
            else:
                count += 1
                trial(res - 1)
        trial(target)
        return count



        