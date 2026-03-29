class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []
        def trial(num):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
    
            for i in range(len(num)):
                if i - 1 >= 0 and num[i - 1] == num[i]:
                    continue
                path.append(num[i])
                trial(num[i + 1:])
                path.pop()
        trial(candidates)
        return res

        