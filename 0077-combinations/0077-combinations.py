class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        def trial(num):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(len(num)):
                path.append(num[i])
                trial(num[i + 1:])
                path.pop()
        trial([i for i in range(1 , n + 1)])
        return res








        # path = []
        # res = []
        # def trial(num):
        #     if len(path ) == k:
        #         res.append(path[:])
        #         return 
        #     for i in range(len(num)):
        #         path.append(num[i])
        #         trial(num[i+1:])
        #         path.remove(num[i])
        #     return 
        # arr = [i for i in range(1, n + 1)]
        # trial(arr)
        # return res
        


        # path = []
        # res = []
        # def drive(num):
        #     if len(path) == k:
        #         res.append(path[:])
        #         return
        #     for i in range(len(num)):
        #         path.append(num[i])
        #         drive(num[i + 1:])
        #         path.pop()
        #     return
        # arr=[i for i in range(1, n + 1)]
        # drive(arr)
        # return res 

        