class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s1= Counter(s)
        l = []
        for i in order:
            while i in s1:
                l.append(i)
                s1[i] -= 1
                if s1[i] == 0:
                    del s1[i]
        for t, k in s1.items():
            l.extend([t] * k)
        return "".join(l)

        