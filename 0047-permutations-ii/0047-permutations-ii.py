class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path= []
        res = []
        def trial(num):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(num)):
                if i -1 >=0 and num[i -1] == num[i]:
                    continue
                path.append(num[i])
                trial(num[:i] + num[i +1:])
                path.pop()
        trial(nums)
        return res

        