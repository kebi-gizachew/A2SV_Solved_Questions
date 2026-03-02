class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        arr = [int(x) for x in s]
        for i in range(1 , len(s)):
            arr[i] += arr[i - 1]
        for t in range(len(arr) - 1):
            y = arr[-1] - arr[t]
            x = t - arr[t] + 1
            m = max(m , y + x)
        return m

        