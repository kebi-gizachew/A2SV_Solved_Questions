n , m = list(map(int , input().split()))
from collections import Counter
l = list(map(int , input().split()))
i = 0
c = Counter()
op = 0
for r in range(len(l)):
    c[l[r]] += 1
    while len(c) > m:
        c[l[i]] -= 1
        if c[l[i]] == 0:
            del c[l[i]]
        i+= 1
    op += r - i + 1
print(op)
