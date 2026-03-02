n = int(input())
from collections import Counter
for _ in range(n):
    m = int(input())
    a = input()
    b = input()
    c = Counter(a)
    flag = True
    sol = True
    for i in range(m -1 , -1 , -1):
        if flag and a[i] != b[i] :
            if c["0"]==c["1"]:
                flag = not flag
            else:
                sol = False
                break
        elif not flag and a[i] ==b[i]:
            if c["0"]==c["1"]:
                flag = not flag
            else:
                sol = False
                break
        c[a[i]] -= 1
    if not sol:
        print("NO")
    else:
        print("YES")
