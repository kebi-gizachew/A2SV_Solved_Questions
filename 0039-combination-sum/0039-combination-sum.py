class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def trial(num , i):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            if i >= len(candidates):
                return
            path.append(num[i])
            trial(num , i)
            path.pop()
            trial(num , i + 1)
        trial(candidates , 0)
        return res
            
        