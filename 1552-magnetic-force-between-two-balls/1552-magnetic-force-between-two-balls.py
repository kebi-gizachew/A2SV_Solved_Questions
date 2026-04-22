class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        ans = -1
        def checking(mid):
            balls = 1
            gap = 0
            for t in range(1 , len(position)):
                gap += position[t] - position[t - 1]
                if gap >= mid:
                    balls += 1
                    gap = 0
            return balls >= m

        while left<= right:
            mid = left + (right - left) // 2
            if checking(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans



        # position.sort()
        # left = 1
        # right = position[-1] - position[0]
        # ans = 0

        # def checking(mid):
        #     count = 1
        #     element = position[0]
        #     for i in range(len(position)):
        #         if position[i] - element >= mid:
        #             count += 1
        #             element = position[i]
        #     return count >= m

        #     # count = 0
        #     # for i in range(0, len(position) , mid):
        #     #     count += 1
        #     # if count >= m:
        #     #     return True
        #     # return False

        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if checking(mid):
        #         ans = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return ans

        # # return (max(position) - min(position)) // (m - 1)
        # # position.sort()
        # # maxx = 0
        # # path = []
        # # def trial(nums):
        # #     nonlocal maxx
        # #     if len(path) == m:
        # #         minn = float("inf")
        # #         for t in range(len(path) - 1):
        # #             minn = min(abs(path[t] - path[t + 1]) ,minn)
        # #         maxx = max(maxx , minn)
        # #         return

        # #     for i in range(len(nums)):
        # #         path.append(nums[i])
        # #         trial(nums[i + 1:])
        # #         path.pop()
        # # trial(position)
        # # return maxx
