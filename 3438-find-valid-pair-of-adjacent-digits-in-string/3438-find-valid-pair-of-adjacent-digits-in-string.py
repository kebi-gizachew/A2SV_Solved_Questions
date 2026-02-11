class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        t = ""
        for i in range(1 , len(s)):
            if str(count[s[i - 1]]) == s[i - 1] and str(count[s[i]]) == s[i] and s[i -1] != s[i]:
                return s[i - 1] + s[i]
        return ""

        