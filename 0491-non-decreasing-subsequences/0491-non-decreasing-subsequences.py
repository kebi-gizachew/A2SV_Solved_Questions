class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = set()
        def trial(num):
            if len(path) >= 2:
                for k in range(len(path) - 1):
                    if path[k + 1] < path[k]:
                        return
                res.add(tuple(path[:]))

            for i in range(len(num)):
                path.append(num[i])
                trial(num[i + 1 :])
                path.pop()
        trial(nums)
        return list(res)






        # path = []
        # res = []
        # def trial(num):
        #     if len(path) >= 2 and path[-1] < path[-2]:
        #         return
        #     if len(path) >= 2:
        #         res.append(path[:])
        #     for i in range(len(num)):
        #         if i - 1 >=0 and num[i] == num[i -1]:
        #             continue
        #         path.append(num[i])
        #         trial(num[i + 1:])
        #         path.pop()
        # trial(nums)
        # return res

                
        