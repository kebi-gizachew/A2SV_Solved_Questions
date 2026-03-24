class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        def drive(num):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(len(num)):
                path.append(num[i])
                drive(num[i + 1:])
                path.pop()
            return
        arr=[i for i in range(1, n + 1)]
        drive(arr)
        return res 

        