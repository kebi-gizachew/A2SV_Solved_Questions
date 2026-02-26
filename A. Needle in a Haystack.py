from collections import Counter
n = int(input())
for _ in range(n):
    a = input()
    b = input()
    if Counter(b) >= Counter(a):
        c = Counter(b) - Counter(a)
        arr = []
        for i , j in c.items():
            for k in range(j):
                arr.append(i)
        arr.sort()
        r = []
        t = 0
        for i in a:
            while t < len(arr) and i>arr[t]:
                r.append(arr[t])
                t += 1
            r.append(i)

        u = "".join(r)
        f = "".join(arr[t:])
        print(u + f)
    else:
        print("Impossible")
