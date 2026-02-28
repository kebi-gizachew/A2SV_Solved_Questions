class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        c = Counter()
        t = s[0]
        maxx = 0
        for r in range(len(s)):
            c[s[r]] += 1
            if c[t] < c[s[r]]:
                t = s[r] 
            if r - i + 1 - c[t] > k:
                maxx = max(maxx , r - i)
                c[s[i]] -= 1
                i += 1
            elif r - i + 1 - c[t] <=k:
                maxx = max(maxx , r - i + 1)
        return maxx






        # l, r= 0, 0 
        # c =Counter()
        # m = 0
        # while r< len(s):
        #     c[s[r]] += 1
        #     if r - l + 1 - c[s[l]] > k:
        #         m = max(m , r - 1)
        #         print(m)
        #         c[s[l]] -= 1
        #         if c[s[l]] == 0:
        #             del c[s[l]]
        #         l -= 1
        #     r+=1
        # if m == 0:
        #     return len(s)
        # else:
        #     return m


        