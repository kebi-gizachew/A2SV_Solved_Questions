class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        arr = []
        for i , j in c.items():
            arr.append([i , j])
        arr.sort(key = lambda x : x[1])
        t = ""
        for n, m in arr[::-1]:
            t += n * m
        return t
        