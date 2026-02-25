class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = defaultdict(int)
        arr = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in c:
                c[s[i]] = i
        k = 0
        while k<len(s):
            op = c[s[k]]
            t = s[k]
            m = k
            while m < op:
                if s[m] != t and c[s[m]] > op:
                    op = c[s[m]]
                    t = s[m]
                m += 1
            arr.append(m + 1 - k)
            k = m+ 1
        return arr
            

        