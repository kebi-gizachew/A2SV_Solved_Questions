class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path = []
        def trial(num):
            res.add(tuple(path[:]))
            if len(path) == len(nums):
                return
            for i in range(len(num)):
                path.append(num[i])
                trial(num[i + 1:])
                path.pop()
        trial(nums)
        finale = []
        for i in res:
            finale.append(list(i))
        return finale



        