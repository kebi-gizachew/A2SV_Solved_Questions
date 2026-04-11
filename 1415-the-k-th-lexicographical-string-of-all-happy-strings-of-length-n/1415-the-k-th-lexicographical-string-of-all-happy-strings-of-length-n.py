class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        path = []
        res = []
        def trial(letters , idx):
            nonlocal n
            if len(path) == n:
                for i in range(len(path) - 1):
                    if path[i + 1] == path[i]:
                        return
                res.append("".join(path[:]))
                return
            if idx >= len(letters):
                return
            path.append(letters[idx])
            trial(letters , 0)
            path.pop()
            trial(letters , idx + 1)
        trial("abc" , 0)
        res.sort()
        return res[k- 1] if k - 1 < len(res) else ""

















        # path = []
        # res = []
        # def trial():
        #     if len(path) == n:
        #         for k in range(len(path) - 1 , 0 , -1):
        #             if path[k] == path[k - 1]:
        #                 return
        #         res.append(path[:])
        #         return
        #     for i in ["a" , "b" , "c"]:
        #         path.append(i)
        #         trial()
        #         path.pop()
        # trial()
        # r = ["".join(i) for i in res]
        # r.sort()
        # return r[k - 1] if k -1 < len(r) else ""
