class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = [[] for i in range(10)]
        path = []
        res = []
        num = 97
        for i in arr[2:]:
            i.append(chr(num))
            i.append(chr(num + 1))
            i.append(chr(num + 2))
            if i[-1] == "r" or i[-1] == "y":
                i.append(chr(num + 3))
                num += 4
                continue
            num += 3
        print(arr)
        def finite(i):
            if len(digits) == i:
                res.append("".join(path[:]))
                return

            for k in arr[int(digits[i])]:
                path.append(k)
                finite(i + 1)
                path.pop()
            return
        finite(0)
        return res




            









        