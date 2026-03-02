n = int(input())
from collections import Counter
for _ in range(n):
    k , l = list(map(int, input().split()))
    s = input()
    c = Counter()
    i = 0
    m = float("inf")
    for r in range(len(s)):
        c[s[r]] += 1
        if r - i+ 1 == l:
            m = min(m , c["W"])
            c[s[i]] -= 1
            i += 1
    print(m)
