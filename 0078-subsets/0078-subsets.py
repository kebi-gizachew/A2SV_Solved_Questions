class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def trial(num):
            res.append(path[:])
            if len(path) == len(nums):
                return
            for i in range(len(num)):
                path.append(num[i])
                trial(num[i + 1:])
                path.pop()
        trial(nums)
        
        return res



        