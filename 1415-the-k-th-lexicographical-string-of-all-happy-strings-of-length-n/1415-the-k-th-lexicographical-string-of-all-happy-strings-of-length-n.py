class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        path = []
        res = []
        def trial():
            if len(path) == n:
                for k in range(len(path) - 1 , 0 , -1):
                    if path[k] == path[k - 1]:
                        return
                res.append(path[:])
                return
            for i in ["a" , "b" , "c"]:
                path.append(i)
                trial()
                path.pop()
        trial()
        r = ["".join(i) for i in res]
        r.sort()
        return r[k - 1] if k -1 < len(r) else ""
