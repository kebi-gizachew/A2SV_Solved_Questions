class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = set()
        def trial(num):
            res.add(tuple(path[:]))
            for i in range(len(num)):
                path.append(num[i])
                trial(num[i + 1:])
                path.pop()
        trial(nums)
        combo = []
        for t in res:
            combo.append(list(t))
        return combo


                
        