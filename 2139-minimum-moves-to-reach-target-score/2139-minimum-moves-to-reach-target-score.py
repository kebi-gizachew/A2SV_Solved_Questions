class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        stack = [target]
        while target > 1:
            if maxDoubles == 0:
                return count + target - 1
            if target % 2 == 0:
                target = target // 2
                maxDoubles -=1 
            else:
                target -= 1
            count += 1
        return count





        # while stack:
        #     temp = stack.pop()
        #     if maxDoubles == 0:
        #         count += (temp - 1)
        #         break
        #     elif temp % 2 == 0:
        #         stack.append(temp// 2) if not temp == 1 else pass
        #         maxDoubles -=1 
        #     else:
        #         stack.append(temp - 1)
        #     count += 1
        # return count

        # # def trial(res):
        # #     nonlocal count , maxDoubles
        # #     if res == 1:
        # #         return
        # #     if res % 2== 0 and maxDoubles != 0:
        # #         maxDoubles -= 1
        # #         count += 1
        # #         trial(res // 2)
        # #     else:
        # #         count += 1
        # #         trial(res - 1)
        # # trial(target)
        # # return count



        