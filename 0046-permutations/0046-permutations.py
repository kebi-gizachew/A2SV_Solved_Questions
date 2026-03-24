class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def drive(num):
            if len(nums) == len(path):
                res.append(path[:])
                return
            for i in range(len(num)):
                path.append(num[i])
                t = num[:i] + num[i + 1:]
                drive(t)
                path.pop()
        drive(nums)
        return res

        